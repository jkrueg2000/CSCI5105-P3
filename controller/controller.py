import grpc
from concurrent import futures
import time
import threading
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../proto/src')))
import market_pb2
import market_pb2_grpc

class MarketplaceController(market_pb2_grpc.InternalServiceServicer):
    def __init__(self):
        # Metadata storage
        self.nodes = {}  # node_id -> {"type": type, "address": addr}
        self.health_map = {}  # node_id -> last_timestamp
        self.primary_id = None
        self.lock = threading.Lock()
        
        # Start failure detection thread
        threading.Thread(target=self._monitor_nodes, daemon=True).start()

    def Heartbeat(self, request, context):
        with self.lock:
            node_id = request.node_id
            self.health_map[node_id] = time.time()
            
            # Register new nodes on the fly
            if node_id not in self.nodes:
                self.nodes[node_id] = {"type": request.type, "address": context.peer()}
                print(f"Registered {request.type} node: {node_id}")
                
                # If it's the first storage node, make it Primary
                if request.type == market_pb2.Ping.STORAGE and self.primary_id is None:
                    self.primary_id = node_id
                    print(f"Elected Primary: {node_id}")

        return market_pb2.Pong(healthy=True)

    def _monitor_nodes(self):
        """Background thread to detect crashes"""
        while True:
            time.sleep(5)
            now = time.time()
            with self.lock:
                dead_nodes = [id for id, t in self.health_map.items() if now - t > 10]
                for node_id in dead_nodes:
                    print(f"Node failure detected: {node_id}")
                    self._handle_failure(node_id)

    def _handle_failure(self, node_id):
        """Logic to promote a new primary if the current one dies"""
        del self.health_map[node_id]
        if node_id == self.primary_id:
            self.primary_id = None
            # Find a new storage node to promote
            for nid, info in self.nodes.items():
                if nid in self.health_map and info["type"] == market_pb2.Ping.STORAGE:
                    self.primary_id = nid
                    print(f"New Primary elected: {self.primary_id}")
                    break
        del self.nodes[node_id]

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_InternalServiceServicer_to_server(MarketplaceController(), server)
    server.add_insecure_port('[::]:50050')
    print("Controller started on port 50050...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()