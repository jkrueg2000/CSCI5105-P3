import os
import asyncio
import logging

import grpc
import grpcio_health_checking

import market_pb2
import market_pb2_grpc

from kubernetes_asyncio import client as k8s_client, config as k8s_config
from kubernetes_asyncio.client.rest import ApiException as K8sApiException

STORAGE_TARGET = os.getenv("STORAGE_TARGET", "localhost:50052")


class Controller(market_pb2_grpc.ControllerServiceServicer):
    def __init__(self):
        super().__init__()
        self.primary = None
        self.live_nodes = {}  # id -> (ip, port)
        self._liveness_task = None
        self._stop_liveness = asyncio.Event()

    async def poll_storage_liveness(self, label_selector: str = "app=storage", namespace: str = "default", interval: int = 10, on_update=None):
        """
        Async loop that queries the Kubernetes API for pods matching `label_selector`
        in `namespace` and invokes `on_update(statuses)` with a dict mapping
        pod-name -> {phase, ready, pod_ip}.

        - `on_update` may be a regular function or an async coroutine function.
        - Requires `kubernetes-asyncio` to be installed.
        """          

        # Prefer in-cluster config, fall back to kubeconfig
        try:
            await k8s_config.load_incluster_config()
        except Exception:
            try:
                await k8s_config.load_kube_config()
            except Exception:
                logging.exception("Failed to load Kubernetes config; API calls will likely fail")

        v1 = k8s_client.CoreV1Api()

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

                if on_update:
                    try:
                        if asyncio.iscoroutinefunction(on_update):
                            await on_update(statuses)
                        else:
                            on_update(statuses)
                    except Exception:
                        logging.exception("on_update callback raised an exception")

            except K8sApiException:
                logging.exception("Kubernetes API error while polling storage liveness")
            except Exception:
                logging.exception("Unexpected error while polling storage liveness")

            # wait for interval or until stop requested
            try:
                await asyncio.wait_for(self._stop_liveness.wait(), timeout=interval)
            except asyncio.TimeoutError:
                pass

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