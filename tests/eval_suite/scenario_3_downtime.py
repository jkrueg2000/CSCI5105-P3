import time
import threading
import subprocess
import grpc
import queue

def _wait_for_recovery(stop_event, is_recovered_ref, current_status_ref, label, timeout=60):
    """Block until the prober signals recovery or timeout is hit."""
    wait_start = time.time()
    while not stop_event.is_set():
        if is_recovered_ref[0]:
            break
        # If system never went down (e.g. backup kill), detect that after 10s
        if time.time() - wait_start > 10 and current_status_ref[0]:
            print(f"[{label}] System remained healthy — no client-visible downtime.")
            break
        if time.time() - wait_start > timeout:
            elapsed = time.time() - wait_start
            print(f"[{label}] Warning: System did not recover within {timeout}s! (waited {elapsed:.1f}s)")
            break
        time.sleep(0.5)

def _wait_for_pod_ready(pod_name, timeout=120):
    """Wait until a specific K8s pod is ready."""
    subprocess.run(
        ["kubectl", "wait", "--for=condition=ready", f"pod/{pod_name}", f"--timeout={timeout}s"],
        check=False, capture_output=True
    )

def _validate_data_integrity(wrapper, all_items, label, snapshot=None):
    """
    Validate data integrity after a node failure event.
    
    Checks:
      1. All items are still retrievable (no data loss)
      2. Item fields are non-corrupt (valid prices, versions)
      3. If a pre-failure snapshot is provided, prices have not decreased
         and versions have not gone backwards (monotonicity)
    
    Returns a new snapshot dict {item_id -> (current_price, version)} for use
    in subsequent calls.
    """
    print(f"\n  [{label}] Validating data integrity across {len(all_items)} items...")
    
    lost = []
    corrupt = []
    regression = []
    new_snapshot = {}
    
    for item_id in all_items:
        try:
            item = wrapper.get_item(item_id, timeout=5)
            # Check for empty/missing response
            if not item or not item.item_id:
                lost.append(item_id)
                continue
            
            # Basic sanity: prices and version should be positive
            if item.current_price < 0 or item.version < 1:
                corrupt.append((item_id, f"price={item.current_price}, version={item.version}"))
                continue
            
            new_snapshot[item_id] = (item.current_price, item.version)
            
            # Monotonicity check against pre-failure snapshot
            if snapshot and item_id in snapshot:
                old_price, old_version = snapshot[item_id]
                if item.current_price < old_price:
                    regression.append((item_id, f"price went from {old_price} to {item.current_price}"))
                if item.version < old_version:
                    regression.append((item_id, f"version went from {old_version} to {item.version}"))
                    
        except grpc.RpcError as e:
            lost.append(item_id)
        except Exception as e:
            lost.append(item_id)
    
    retrieved = len(all_items) - len(lost)
    print(f"  [{label}] Items retrieved: {retrieved}/{len(all_items)}")
    
    if lost:
        print(f"  [{label}] FAIL — {len(lost)} items lost: {lost[:5]}{'...' if len(lost) > 5 else ''}")
    if corrupt:
        print(f"  [{label}] FAIL — {len(corrupt)} items corrupt: {corrupt[:5]}")
    if regression:
        print(f"  [{label}] FAIL — {len(regression)} regressions: {regression[:5]}")
    
    if not lost and not corrupt and not regression:
        print(f"  [{label}] PASS — All data intact, no regressions detected.")
    
    return new_snapshot, len(lost), len(corrupt), len(regression)


def run_downtime_scenario(wrapper, workload_manager, all_items=None):
    print("--- Running Scenario 3: Downtime & Recovery ---")
    
    stop_event = threading.Event()
    results = {"backup_kill": [], "primary_kill": []}
    integrity_results = {}
    is_recovered = [False]
    current_status = [True]

    # If no items list provided, use a default range
    if all_items is None:
        all_items = [f"item-{i}" for i in range(100)]

    # Take a pre-test snapshot of all item state
    print("Taking pre-failure data snapshot...")
    snapshot = {}
    for item_id in all_items:
        try:
            item = wrapper.get_item(item_id, timeout=5)
            if item and item.item_id:
                snapshot[item_id] = (item.current_price, item.version)
        except Exception:
            pass
    print(f"Snapshot captured: {len(snapshot)} items\n")

    print("Starting background workload...")
    workload_manager.start(num_getters=20, num_bidders=5)

    def error_processor():
        in_downtime = False
        fail_start = None
        
        while not stop_event.is_set():
            try:
                timestamp, status = workload_manager.error_queue.get(timeout=0.1)
                
                if status == "ERROR":
                    if not in_downtime:
                        fail_start = timestamp
                        print("[Workload] Client error detected, starting downtime timer...")
                        in_downtime = True
                    current_status[0] = False
                elif status == "SUCCESS":
                    if in_downtime and fail_start:
                        downtime = timestamp - fail_start
                        results["_active_list"].append(downtime)
                        print(f"[Workload] Recovered! Downtime: {downtime:.2f}s")
                        fail_start = None
                        is_recovered[0] = True
                        in_downtime = False
                    current_status[0] = True
            except queue.Empty:
                pass
            except Exception:
                pass

    t = threading.Thread(target=error_processor, daemon=True)
    t.start()
    
    print("Waiting 3s for workload to stabilize...")
    time.sleep(3)

    # ---- Phase 1: Kill a backup node ----
    print("\n=== Phase 1: Killing Backup Node ===")
    results["_active_list"] = results["backup_kill"]
    is_recovered[0] = False

    if wrapper.env_type == "k8s":
        subprocess.run(["kubectl", "delete", "pod", "storage-1", "--grace-period=0", "--force"], check=False)
    else:
        subprocess.run(["docker", "kill", "storage-1"], check=False)
    
    _wait_for_recovery(stop_event, is_recovered, current_status, "Backup Kill", timeout=60)

    # Wait for backup to be fully back before validating
    if wrapper.env_type == "k8s":
        print("Waiting for backup pod storage-1 to be recreated and ready...")
        _wait_for_pod_ready("storage-1")
        time.sleep(3)  # extra settle time for controller to re-register it

    # Validate data integrity after backup kill
    snapshot, lost, corrupt, regress = _validate_data_integrity(
        wrapper, all_items, "Post-Backup-Kill", snapshot
    )
    integrity_results["backup_kill"] = {"lost": lost, "corrupt": corrupt, "regressions": regress}

    # ---- Phase 2: Kill the primary node ----
    print("\n=== Phase 2: Killing Primary Node ===")
    results["_active_list"] = results["primary_kill"]
    is_recovered[0] = False

    if wrapper.env_type == "k8s":
        subprocess.run(["kubectl", "delete", "pod", "storage-0", "--grace-period=0", "--force"], check=False)
    else:
        subprocess.run(["docker", "kill", "storage-0"], check=False)

    _wait_for_recovery(stop_event, is_recovered, current_status, "Primary Kill", timeout=60)

    # Wait for primary to be recreated before validating
    if wrapper.env_type == "k8s":
        print("Waiting for primary pod storage-0 to be recreated and ready...")
        _wait_for_pod_ready("storage-0")
        time.sleep(3)

    # Validate data integrity after primary kill
    snapshot, lost, corrupt, regress = _validate_data_integrity(
        wrapper, all_items, "Post-Primary-Kill", snapshot
    )
    integrity_results["primary_kill"] = {"lost": lost, "corrupt": corrupt, "regressions": regress}

    stop_event.set()
    t.join(timeout=3)
    workload_manager.stop()

    # ---- Report ----
    print("\n=== Downtime Summary ===")
    if results["backup_kill"]:
        for i, dt in enumerate(results["backup_kill"]):
            print(f"  Backup Kill Event {i+1}: {dt:.2f}s")
    else:
        print("  Backup Kill: No client-visible downtime (reads route to primary)")

    if results["primary_kill"]:
        for i, dt in enumerate(results["primary_kill"]):
            print(f"  Primary Kill Event {i+1}: {dt:.2f}s")
    else:
        print("  Primary Kill: No downtime recorded (system may not have recovered)")

    print("\n=== Data Integrity Summary ===")
    for phase, res in integrity_results.items():
        label = phase.replace("_", " ").title()
        total_issues = res["lost"] + res["corrupt"] + res["regressions"]
        status = "PASS" if total_issues == 0 else "FAIL"
        print(f"  {label}: {status} (lost={res['lost']}, corrupt={res['corrupt']}, regressions={res['regressions']})")
    print()

