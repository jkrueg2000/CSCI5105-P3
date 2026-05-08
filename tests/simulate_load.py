import argparse
import sys
import os
import time

def main():
    parser = argparse.ArgumentParser(description="Run sustained load test")
    parser.add_argument("--target", choices=["k8s", "docker"], required=True, help="Target architecture to test")
    parser.add_argument("--endpoint", help="gRPC endpoint (defaults to localhost:50051 for k8s and localhost:50050 for docker)")
    parser.add_argument("--getters", type=int, default=50, help="Number of getter clients")
    parser.add_argument("--bidders", type=int, default=10, help="Number of bidder clients")
    args = parser.parse_args()

    # 1. Setup Environment Path
    # We must load the correct proto definitions depending on the target
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    
    if args.target == "k8s":
        proto_path = os.path.join(project_root, "proto", "src")
        endpoint = args.endpoint or "localhost:50051"
    else:
        proto_path = os.path.abspath(os.path.join(project_root, "..", "P3-Docker", "proto", "src"))
        if not os.path.exists(proto_path):
            print(f"Error: Could not find P3-Docker proto path at {proto_path}")
            sys.exit(1)
        endpoint = args.endpoint or "localhost:50050"
    
    sys.path.insert(0, proto_path)

    # 2. Import scenarios
    from eval_suite.client_wrapper import ClientWrapper
    from eval_suite.workload import setup_database, WorkloadManager

    wrapper = ClientWrapper(endpoint, env_type=args.target)

    print(f"===========================================================")
    print(f" Starting Sustained Load Test for target: {args.target.upper()}")
    print(f" Getters: {args.getters} | Bidders: {args.bidders}")
    print(f" Endpoint: {endpoint}")
    print(f"===========================================================\n")

    try:
        bidding_items, all_items = setup_database(wrapper)
        workload_manager = WorkloadManager(wrapper, bidding_items, all_items)
        
        print(f"\nStarting Workload Manager...")
        workload_manager.start(num_getters=args.getters, num_bidders=args.bidders)
        
        print(f"Press Ctrl+C to stop.\n")
        
        last_requests = 0
        while True:
            time.sleep(1.0)
            current_requests = workload_manager.counter.get()
            rps = current_requests - last_requests
            last_requests = current_requests
            
            get_avg = workload_manager.get_averager.get_avg() * 1000
            search_avg = workload_manager.search_averager.get_avg() * 1000
            bid_avg = workload_manager.bid_averager.get_avg() * 1000
            
            get_sr = workload_manager.get_averager.get_success_rate()
            search_sr = workload_manager.search_averager.get_success_rate()
            bid_sr = workload_manager.bid_averager.get_success_rate()
            
            # Create a simple visual bar (scale 1 block = 50 requests, max 15)
            bar_len = min(int(rps / 50), 15) 
            bar = '#' * bar_len
            
            # Print the bar chart and latencies, overwriting the current line
            sys.stdout.write(f"\rRPS: {rps:5d} | Get: {get_avg:5.1f}ms ({get_sr:3.0f}%) | Search: {search_avg:5.1f}ms ({search_sr:3.0f}%) | Bid: {bid_avg:5.1f}ms ({bid_sr:3.0f}%) |{bar.ljust(15)}|")
            sys.stdout.flush()

    except KeyboardInterrupt:
        print("\n\nStopping Workload Manager...")
        workload_manager.stop()
        print("Done.")
    except Exception as e:
        print(f"\n\nEncountered an error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
