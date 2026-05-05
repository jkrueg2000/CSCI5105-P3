import grpc
from concurrent import futures
import time
import threading
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../proto/src')))
import market_pb2
import market_pb2_grpc
import random

class MarketplaceController(market_pb2_grpc.InternalServiceServicer):
    def __init__(self):
        # Metadata storage
        self.nodes = {}  # node_id -> {"type": type, "address": addr}
        self.health_map = {}  # node_id -> last_timestamp
        self.primary_id = None
        self.lock = threading.Lock()
        
        # Start failure detection thread
        threading.Thread(target=self._monitor_nodes, daemon=True).start()

    def CreateItem(self, request, context):
        service_node = self._get_random_service_node()
        if not service_node:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return market_pb2.ActionResponse(success=False, message="No service nodes available")
        
        return service_node["stub"].CreateItem(request)

    def GetItem(self, request, context):
        service_node = self._get_random_service_node()
        if not service_node:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return market_pb2.MarketplaceItem()
        
        return service_node["stub"].GetItem(request)
    
    def UpdateItem(self, request, context):
        service_node = self._get_random_service_node()
        if not service_node:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return market_pb2.MarketplaceItem()
        
        return service_node["stub"].UpdateItem(request)
    
    def SearchItems(self, request, context):
        service_node = self._get_random_service_node()
        if not service_node:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return market_pb2.MarketplaceItem()
        
        return service_node["stub"].SearchItems(request)

    def PlaceBid(self, request, context):
        service_node = self._get_random_service_node()
        if not service_node:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return market_pb2.MarketplaceItem()
        
        return service_node["stub"].PlaceBid(request)
    
    def JoinAuction(self, request, context):
        service_node = self._get_random_service_node()
        if not service_node:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return market_pb2.MarketplaceItem()
        
        yield from service_node["stub"].JoinAuction(request)

    def _get_random_service_node(self):
        """Simple Load Balancer"""
        with self.lock:
            services = [n for id, n in self.nodes.items() if n["type"] == market_pb2.Ping.SERVICE]
            return random.choice(services) if services else None

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
        node_info = self.nodes.pop(node_id, None)
        self.health_map.pop(node_id, None)
        
        if node_info and node_info["type"] == market_pb2.Ping.STORAGE:
            print(f"Storage node {node_id} removed")
            if node_id == self.primary_id:
                print("Primary failed! Initiating new election...")
                self.primary_id = None
                # Elect new primary if possible
                for id, info in self.nodes.items():
                    if info["type"] == market_pb2.Ping.STORAGE:
                        self.primary_id = id
                        print(f"New Primary elected: {id}")
                        break

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_InternalServiceServicer_to_server(MarketplaceController(), server)
    server.add_insecure_port('[::]:50050')
    print("Controller started on port 50050...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()