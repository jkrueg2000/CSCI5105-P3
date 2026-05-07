#!/usr/bin/env python3
import os
import sys
import time
import threading
import grpc
import argparse

import market_pb2
import market_pb2_grpc

stop_event = threading.Event()
requests_completed = 0
lock = threading.Lock()

def worker(target, item_id):
    global requests_completed
    try:
        with grpc.insecure_channel(target) as channel:
            stub = market_pb2_grpc.MarketplaceServiceStub(channel)
            while not stop_event.is_set():
                try:
                    # Perform a GetItem request to simulate load
                    stub.GetItem(market_pb2.GetItemRequest(item_id=item_id), timeout=2)
                    with lock:
                        requests_completed += 1
                except grpc.RpcError:
                    pass # ignore intermittent failures under heavy load
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default=os.environ.get("SERVICE_TARGET", "localhost:50051"))
    parser.add_argument("--workers", type=int, default=20)
    parser.add_argument("--duration", type=int, default=10)
    parser.add_argument("--item", default="test-item-123")
    args = parser.parse_args()

    print(f"Starting load test with {args.workers} workers for {args.duration}s against {args.target}")
    
    threads = []
    for _ in range(args.workers):
        t = threading.Thread(target=worker, args=(args.target, args.item))
        t.start()
        threads.append(t)

    start_time = time.time()
    time.sleep(args.duration)
    stop_event.set()

    for t in threads:
        t.join()
        
    actual_duration = time.time() - start_time
    rps = requests_completed / actual_duration
    
    print(f"Total Requests: {requests_completed}")
    print(f"Duration: {actual_duration:.2f}s")
    print(f"RPS (Throughput): {rps:.2f} req/s")

if __name__ == "__main__":
    main()
