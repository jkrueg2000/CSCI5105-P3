import time

def run_throughput_scenario(wrapper, workload_manager, duration=10, num_getters=20, num_bidders=5):
    print(f"--- Running Scenario 1: Throughput ({num_getters} getters, {num_bidders} bidders) ---")
    
    start_time = time.time()
    workload_manager.start(num_getters=num_getters, num_bidders=num_bidders)
    
    time.sleep(duration)
    
    workload_manager.stop()
    
    actual_duration = time.time() - start_time
    total_requests = workload_manager.counter.get()
    rps = total_requests / actual_duration
    
    print(f"Total Requests (Reads + Bids + Stream Events): {total_requests}")
    print(f"Duration: {actual_duration:.2f}s")
    print(f"RPS: {rps:.2f} req/s\n")
    return rps
