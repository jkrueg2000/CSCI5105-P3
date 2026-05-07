import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Run Evaluation Suite against K8s or Docker architecture")
    parser.add_argument("--target", choices=["k8s", "docker"], required=True, help="Target architecture to test")
    parser.add_argument("--endpoint", help="gRPC endpoint (defaults to localhost:50051 for k8s and localhost:50050 for docker)")
    args = parser.parse_args()

    # 1. Setup Environment Path
    # We must load the correct proto definitions depending on the target
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if args.target == "k8s":
        proto_path = os.path.join(base_dir, "proto", "src")
        endpoint = args.endpoint or "localhost:50051"
    else:
        # Assuming P3-Docker is located in a sibling directory named 'P3-Docker'
        proto_path = os.path.abspath(os.path.join(base_dir, "..", "P3-Docker", "proto", "src"))
        if not os.path.exists(proto_path):
            print(f"Error: Could not find P3-Docker proto path at {proto_path}")
            sys.exit(1)
        endpoint = args.endpoint or "localhost:50050"
    
    sys.path.insert(0, proto_path)

    # 2. Import scenarios
    # We do this AFTER sys.path modification so they import the correct market_pb2
    from eval_suite.client_wrapper import ClientWrapper
    from eval_suite.scenario_1_throughput import run_throughput_scenario
    from eval_suite.scenario_2_scaling import run_scaling_scenario
    from eval_suite.scenario_3_downtime import run_downtime_scenario
    from eval_suite.scenario_4_consistency import run_consistency_scenario

    wrapper = ClientWrapper(endpoint, env_type=args.target)

    print(f"===========================================================")
    print(f" Starting Evaluation Suite for target: {args.target.upper()}")
    print(f" Endpoint: {endpoint}")
    print(f"===========================================================\n")

    try:
        run_throughput_scenario(wrapper)
        run_scaling_scenario(wrapper)
        run_downtime_scenario(wrapper)
        run_consistency_scenario(wrapper)
    except Exception as e:
        print(f"Evaluation suite encountered an error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
