import os
import asyncio
import logging

import grpc
from grpc_health.v1 import health, health_pb2, health_pb2_grpc

import market_pb2
import market_pb2_grpc

from kubernetes_asyncio import client as k8s_client, config as k8s_config
from kubernetes_asyncio.client.rest import ApiException as K8sApiException

from utils.logging_config import configure_logging

# Configure root logger (idempotent)
configure_logging()

logger = logging.getLogger(__name__)

STORAGE_TARGET = os.getenv("STORAGE_TARGET", "localhost:50052")
PORT = os.environ.get("PORT", "50050")
POD_NAME = os.environ.get("POD_NAME", "controller")


class Controller(market_pb2_grpc.ControllerServiceServicer):
    def __init__(self):
        super().__init__()
        self.primary = None
        self.live_nodes = {}  # id -> (ip, port)
        self._liveness_task = None
        self._stop_liveness = asyncio.Event()
        self._api_client = None
        self._v1 = None

    async def poll_storage_liveness(self, label_selector: str = "app=storage", namespace: str = "default", interval: int = 3, on_update=None):
        """
        Async loop that queries the Kubernetes API for pods matching `label_selector`
        in `namespace` and invokes `on_update(statuses)` with a dict mapping
        pod-name -> {phase, ready, pod_ip}.

        - `on_update` may be a regular function or an async coroutine function.
        - Requires `kubernetes-asyncio` to be installed.
        """          

        # Prefer in-cluster config, fall back to kubeconfig
        try:
            k8s_config.load_incluster_config()
        except Exception:
            try:
                await k8s_config.load_kube_config()
            except Exception:
                logging.exception("Failed to load Kubernetes config; API calls will likely fail")

        self._api_client = k8s_client.ApiClient()
        self._v1 = k8s_client.CoreV1Api(self._api_client)
        v1 = self._v1

        try:
            while not self._stop_liveness.is_set():
                try:
                    pods = await v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
                    statuses = {}
                    for pod in pods.items:
                        name = getattr(pod.metadata, "name", None)
                        phase = getattr(pod.status, "phase", None)
                        pod_ip = getattr(pod.status, "pod_ip", None)
                        conditions = getattr(pod.status, "conditions", []) or []
                        ready_cond = next((c for c in conditions if getattr(c, "type", "") == "Ready"), None)
                        ready = getattr(ready_cond, "status", "") == "True" if ready_cond else False
                        statuses[name] = {"phase": phase, "ready": ready, "pod_ip": pod_ip}

                    self.live_nodes = statuses
                    await self._elect_primary(statuses, namespace)

                except K8sApiException:
                    logging.exception("Kubernetes API error while polling storage liveness")
                except Exception:
                    logging.exception("Unexpected error while polling storage liveness")

                # wait for interval or until stop requested
                try:
                    await asyncio.wait_for(self._stop_liveness.wait(), timeout=interval)
                except asyncio.TimeoutError:
                    pass
        finally:
            await self._api_client.close()

    def start_storage_liveness_poll(self, *args, **kwargs):
        """
        Start the background liveness polling task. Must be called from within an
        active asyncio event loop. Returns the created Task.
        """
        if self._liveness_task and not self._liveness_task.done():
            logging.debug("storage liveness poll already running")
            return self._liveness_task
        self._stop_liveness.clear()
        loop = asyncio.get_event_loop()
        self._liveness_task = loop.create_task(self.poll_storage_liveness(*args, **kwargs))
        return self._liveness_task

    async def stop_storage_liveness_poll(self):
        """Signal the polling loop to stop and wait for the task to finish."""
        if not self._liveness_task:
            return
        self._stop_liveness.set()
        try:
            await self._liveness_task
        except Exception:
            try:
                self._liveness_task.cancel()
            except Exception:
                pass
        finally:
            self._liveness_task = None
            self._stop_liveness = asyncio.Event()

    async def _elect_primary(self, statuses, namespace="default"):
        v1 = self._v1
        if not v1:
            logging.error("K8s API client not initialized, skipping election")
            return
        # candidates = ready Running pods with an IP
        candidates = [name for name, s in statuses.items() if s["phase"] == "Running" and s["ready"] and s.get("pod_ip")]
        if not candidates:
            logging.warning("No ready storage candidates for election")
            return
        
        # If the current primary is still healthy, ensure its label is applied
        # (handles the case where StatefulSet recreated the pod with the same name
        # but without the role=primary label)
        if self.primary and self.primary in candidates:
            body = {"metadata": {"labels": {"role": "primary"}}}
            try:
                await v1.patch_namespaced_pod(self.primary, namespace, body)
            except Exception:
                logging.debug("failed to re-apply primary label on %s", self.primary)
            return

        logging.info("Primary %s is no longer a candidate. Candidates: %s", self.primary, candidates)

        # Current primary is gone or not yet set — elect the first available candidate
        # (prefer lowest ordinal only as a tiebreaker)
        def ordinal(n):
            try:
                return int(n.rsplit("-", 1)[1])
            except Exception:
                return 999
            
        candidates.sort(key=ordinal)
        chosen = candidates[0]

        # set the new primary label
        body = {"metadata": {"labels": {"role": "primary"}}}
        try:
            await v1.patch_namespaced_pod(chosen, namespace, body)
            logging.info("Patched role=primary label onto %s", chosen)
        except Exception:
            logging.exception("FAILED to set primary label on %s", chosen)
            return  # Don't update self.primary if the patch failed

        # remove role label from previous primary (if any) using JSON patch
        if self.primary and self.primary != chosen:
            try:
                patch = [{"op": "remove", "path": "/metadata/labels/role"}]
                await v1.patch_namespaced_pod(self.primary, namespace, patch, _content_type="application/json-patch+json")
            except Exception:
                logging.debug("old primary label removal failed (may be already absent)")

        self.primary = chosen
        logging.info("Elected new primary: %s", chosen)

    async def GetBackup(self, request, context):
        if not self.primary:
            return market_pb2.BackupResponse()
        primary_info = self.live_nodes.get(self.primary)
        if not primary_info or not primary_info.get("pod_ip"):
            return market_pb2.BackupResponse()
        
        target = f"{primary_info['pod_ip']}:50052"
        try:
            async with grpc.aio.insecure_channel(target) as channel:
                stub = market_pb2_grpc.StorageServiceStub(channel)
                return await stub.GetBackup(request, timeout=5)
        except Exception as e:
            logger.exception("Failed to get backup from primary")
            return market_pb2.BackupResponse()

    async def _relay_to_secondaries(self, rpc_name, request):
        secondaries = [info for name, info in self.live_nodes.items() if name != self.primary and info.get("phase") == "Running" and info.get("pod_ip")]
        if not secondaries:
            return market_pb2.ActionResponse(success=True, message="no secondaries", new_version=0)
        
        # Mark as replica write
        request.is_replica_write = True
        
        tasks = []
        for info in secondaries:
            target = f"{info['pod_ip']}:50052"
            async def call_node(tgt):
                try:
                    async with grpc.aio.insecure_channel(tgt) as channel:
                        stub = market_pb2_grpc.StorageServiceStub(channel)
                        method = getattr(stub, rpc_name)
                        return await method(request, timeout=5)
                except Exception:
                    return None
            tasks.append(call_node(target))
            
        results = await asyncio.gather(*tasks)
        successes = [r for r in results if r and getattr(r, "success", False)]
        if len(successes) == len(secondaries): # simple majority or half
            return market_pb2.ActionResponse(success=True, message="replicated", new_version=successes[0].new_version if successes else 0)
        else:
            return market_pb2.ActionResponse(success=False, message="replication failed", new_version=0)
            

    async def CreateItemBackup(self, request, context):
        return await self._relay_to_secondaries("CreateItem", request)

    async def UpdateBackups(self, request, context):
        return await self._relay_to_secondaries("UpdateItem", request)

    async def BidUpdateBackups(self, request, context):
        return await self._relay_to_secondaries("PlaceBid", request)


async def serve():
    server = grpc.aio.server()
    controller_servicer = Controller()
    market_pb2_grpc.add_ControllerServiceServicer_to_server(controller_servicer, server)

    # Health servicer for Kubernetes gRPC probes
    health_servicer = health.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
    # Mark server as serving for overall health
    health_servicer.set("", health_pb2.HealthCheckResponse.SERVING)

    server.add_insecure_port(f"[::]:{PORT}")
    await server.start()
    logger.info("controller %s listening on %s", POD_NAME, PORT)
    
    # Start the polling loop
    controller_servicer.start_storage_liveness_poll()

    try:
        await server.wait_for_termination()
    finally:
        try:
            health_servicer.set("", health_pb2.HealthCheckResponse.NOT_SERVING)
        except Exception:
            pass


if __name__ == "__main__":
    import asyncio
    asyncio.run(serve())