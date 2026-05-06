import time

import docker
import docker.errors
import grpc
import numpy as np
from market_pb2 import *


def wait_for_grpc_target(target: str, retry_seconds: float = 0.5) -> None:
    while True:
        try:
            with grpc.insecure_channel(target) as channel:
                grpc.channel_ready_future(channel).result(timeout=1)
            return
        except grpc.FutureTimeoutError:
            time.sleep(retry_seconds)
        except grpc.RpcError:
            time.sleep(retry_seconds)

# Needs Modification
def create_storage_node(node_num: int) -> str:
    client = docker.from_env()
    name: str = f"storage-node-{node_num}"
    target: str = f"{name}:{NODE_PORT}"

    try:
        client.containers.get(name).remove(force=True)
    except docker.errors.NotFound:
        pass

    client.containers.run(
        DOCKER_IMAGE,
        name=name,
        hostname=name,
        network=DOCKER_NETWORK,
        detach=True,
        working_dir="/app",
        command=["python", "-u", "storage_node/node.py"],
        environment={
            "GRPC_SERVER_PORT": str(NODE_PORT),
            "NODE_TARGET": target,
            "PYTHONPATH": "/app:/app/proto/src",
        },
    )
    wait_for_grpc_target(target)
    return target
