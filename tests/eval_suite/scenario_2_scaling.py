import subprocess
import time
from .scenario_1_throughput import run_throughput_scenario

def run_scaling_scenario(wrapper, workload_manager):
    print("--- Running Scenario 2: Kubernetes Scaling ---")
    
    if wrapper.env_type != "k8s":
        print("Skipping scaling scenario for non-k8s environment as requested.")
        return

    print("Baseline Test (Current Replicas):")
    print("Ensuring 1 frontend replica for baseline test...")
    subprocess.run(["kubectl", "scale", "deployment/frontend", "--replicas=1"], check=True)
    subprocess.run(["kubectl", "wait", "--for=condition=ready", "pod", "-l", "app=frontend", "--timeout=60s"], check=True)
    baseline_rps = run_throughput_scenario(wrapper, workload_manager, duration=10, num_getters=100, num_bidders=10)

    print("Scaling K8s deployment frontend to 10 replicas...")
    subprocess.run(["kubectl", "scale", "deployment/frontend", "--replicas=10"], check=True)
    
    print("Waiting for pods to be ready...")
    time.sleep(5)
    subprocess.run(["kubectl", "wait", "--for=condition=ready", "pod", "-l", "app=frontend", "--timeout=60s"], check=True)

    print("Scaled Test (10 Replicas):")
    # Need to wait a moment for internal DNS/load balancers to register the new endpoints
    time.sleep(5) 
    scaled_rps = run_throughput_scenario(wrapper, workload_manager, duration=10, num_getters=100, num_bidders=10)

    print(f"Scaling Results: Baseline={baseline_rps:.2f} rps, Scaled={scaled_rps:.2f} rps")
    
    # Reset back to 1 for subsequent tests
    subprocess.run(["kubectl", "scale", "deployment/frontend", "--replicas=1"], check=True)
    subprocess.run(["kubectl", "wait", "--for=condition=ready", "pod", "-l", "app=frontend", "--timeout=60s"], check=True)
