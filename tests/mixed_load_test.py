#!/usr/bin/env python3
import os
import sys
import time
import threading
import random
import grpc
import argparse

import market_pb2
import market_pb2_grpc

stop_event = threading.Event()
requests_completed = 0
lock = threading.Lock()

def worker(target, item_id, write_ratio):
    global requests_completed
    try:
        with grpc.insecure_channel(target) as channel:
            stub = market_pb2_grpc.MarketplaceServiceStub(channel)
            while not stop_event.is_set():
                try:
                    if random.random() < write_ratio:
                        # Perform a PlaceBid request to simulate write load
                        # Use a random bid amount to keep it dynamic
                        bid_req = market_pb2.BidRequest(
                            item_id=item_id,
                            bidder_id=f"bidder-{random.randint(1000, 9999)}",
                            bid_amount=round(random.uniform(10.0, 500.0), 2)
                        )
                        stub.PlaceBid(bid_req, timeout=2)
                    else:
                        # Perform a GetItem request to simulate read load
                        stub.GetItem(market_pb2.GetItemRequest(item_id=item_id), timeout=2)
                    
                    with lock:
                        requests_completed += 1
                except grpc.RpcError:
                    pass # ignore intermittent failures under heavy load
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="Mixed read/write load test for the distributed marketplace")
    parser.add_argument("--target", default=os.environ.get("SERVICE_TARGET", "localhost:50051"))
    parser.add_argument("--workers", type=int, default=20)
    parser.add_argument("--duration", type=int, default=10)
    parser.add_argument("--item", default="test-item-123")
    parser.add_argument("--write-ratio", type=float, default=0.1, help="Ratio of requests that should be writes (0.0 to 1.0)")
    args = parser.parse_args()

    print(f"Starting mixed load test with {args.workers} workers for {args.duration}s against {args.target}")
    print(f"Write Ratio: {args.write_ratio:.0%} Bids, {1 - args.write_ratio:.0%} Gets")
    
    threads = []
    for _ in range(args.workers):
        t = threading.Thread(target=worker, args=(args.target, args.item, args.write_ratio))
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
