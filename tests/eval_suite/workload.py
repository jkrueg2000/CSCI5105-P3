import threading
import time
import random
import multiprocessing
import ctypes
import queue
import os
import grpc
import market_pb2

def setup_database(wrapper, total_items=100, bidding_items=10):
    print(f"Setting up database with {total_items} items ({bidding_items} for bidding)...")
    item_ids = [f"item-{i}" for i in range(total_items)]
    for i, item_id in enumerate(item_ids):
        item = market_pb2.MarketplaceItem(
            item_id=item_id,
            seller_id=f"seller-{i}",
            title=f"Test Item {i}",
            category="bidding" if i < bidding_items else "standard",
            description=f"Description for item {i}",
            starting_price=10.0,
            current_price=10.0,
            quantity=1,
            status="AUCTION_ACTIVE",
            version=1
        )
        try:
            wrapper.create_item(item, timeout=2)
        except Exception as e:
            pass
            
    bidding_item_ids = item_ids[:bidding_items]
    return bidding_item_ids, item_ids

class Counter:
    def __init__(self):
        self.val = 0
        self.lock = threading.Lock()
    def inc(self):
        with self.lock:
            self.val += 1
    def get(self):
        with self.lock:
            return self.val

class Averager:
    def __init__(self):
        self.total = 0.0
        self.success_count = 0
        self.attempt_count = 0
        self.lock = threading.Lock()
    def add_attempt(self):
        with self.lock:
            self.attempt_count += 1
    def add_success(self, val):
        with self.lock:
            self.total += val
            self.success_count += 1
    def get_avg(self):
        with self.lock:
            return (self.total / self.success_count) if self.success_count > 0 else 0.0
    def get_success_rate(self):
        with self.lock:
            return (self.success_count / self.attempt_count) * 100.0 if self.attempt_count > 0 else 0.0
            
    def get_raw_stats(self):
        with self.lock:
            return self.total, self.success_count, self.attempt_count

class GetterClient(threading.Thread):
    def __init__(self, target, env_type, all_item_ids, error_queue, counter, get_averager, search_averager, stop_event):
        super().__init__(daemon=True)
        self.target = target
        self.env_type = env_type
        self.all_item_ids = all_item_ids
        self.stop_event = stop_event
        self.error_queue = error_queue
        self.counter = counter
        self.get_averager = get_averager
        self.search_averager = search_averager

    def run(self):
        from eval_suite.client_wrapper import ClientWrapper
        self.wrapper = ClientWrapper(self.target, self.env_type)
        while not self.stop_event.is_set():
            try:
                if random.random() < 0.5:
                    item_id = random.choice(self.all_item_ids)
                    if self.get_averager:
                        self.get_averager.add_attempt()
                    start = time.time()
                    self.wrapper.get_item(item_id, timeout=2)
                    duration = time.time() - start
                    if self.get_averager:
                        self.get_averager.add_success(duration)
                else:
                    if self.search_averager:
                        self.search_averager.add_attempt()
                    start = time.time()
                    self.wrapper.search_items(query="Test", category="", timeout=2)
                    duration = time.time() - start
                    if self.search_averager:
                        self.search_averager.add_success(duration)
                
                if self.counter:
                    self.counter.inc()
                if self.error_queue is not None:
                    self.error_queue.put((time.time(), "SUCCESS"))
            except grpc.RpcError:
                if self.error_queue is not None:
                    self.error_queue.put((time.time(), "ERROR"))
            except Exception:
                pass

class BidderClient(threading.Thread):
    def __init__(self, target, env_type, bidding_item_ids, client_id, error_queue, counter, bid_averager, stop_event):
        super().__init__(daemon=True)
        self.target = target
        self.env_type = env_type
        self.bidding_item_ids = bidding_item_ids
        self.client_id = client_id
        self.stop_event = stop_event
        self.error_queue = error_queue
        self.counter = counter
        self.bid_averager = bid_averager
        self.current_prices = {item_id: 10.0 for item_id in bidding_item_ids}
        self.streams = []

    def run(self):
        from eval_suite.client_wrapper import ClientWrapper
        self.wrapper = ClientWrapper(self.target, self.env_type)
        for item_id in self.bidding_item_ids:
            t = threading.Thread(target=self._watch_item, args=(item_id,), daemon=True)
            t.start()
            self.streams.append(t)

        while not self.stop_event.is_set():
            try:
                item_id = random.choice(self.bidding_item_ids)
                current_price = self.current_prices[item_id]
                bid_increment = abs(random.gauss(2.0, 1.0)) 
                bid_amount = round(current_price + bid_increment, 2)
                
                if self.bid_averager:
                    self.bid_averager.add_attempt()
                start = time.time()
                resp = self.wrapper.place_bid(item_id, self.client_id, bid_amount, timeout=2)
                duration = time.time() - start
                
                if getattr(resp, 'success', False):
                    # Immediately update our local price so the next bid is above the new price
                    self.current_prices[item_id] = bid_amount
                    if self.bid_averager:
                        self.bid_averager.add_success(duration)
                else:
                    # Bid failed (likely stale price) — fetch the real current price to resync
                    try:
                        item = self.wrapper.get_item(item_id, timeout=2)
                        if item and item.current_price > 0:
                            self.current_prices[item_id] = item.current_price
                    except Exception:
                        pass
                
                if self.counter:
                    self.counter.inc()
                if self.error_queue is not None:
                    self.error_queue.put((time.time(), "SUCCESS"))
            except grpc.RpcError:
                if self.error_queue is not None:
                    self.error_queue.put((time.time(), "ERROR"))
            except Exception:
                pass

    def _watch_item(self, item_id):
        while not self.stop_event.is_set():
            try:
                stream = self.wrapper.join_auction(item_id, self.client_id)
                for event in stream:
                    if self.stop_event.is_set():
                        break
                    if event.HasField('item_snapshot') and event.item_snapshot.current_price > self.current_prices[item_id]:
                        self.current_prices[item_id] = event.item_snapshot.current_price
                    
                    if self.counter:
                        self.counter.inc()
                    if self.error_queue is not None:
                        self.error_queue.put((time.time(), "SUCCESS"))
            except grpc.RpcError:
                if self.error_queue is not None:
                    self.error_queue.put((time.time(), "ERROR"))
                time.sleep(0.5)
            except Exception:
                time.sleep(0.5)

def run_worker_process(worker_id, target, env_type, all_items, bidding_items, num_getters, num_bidders, 
                       shared_counter, shared_get, shared_search, shared_bid, stop_event):
    # Pure Python fast local counters for the hot path
    local_counter = Counter()
    local_get = Averager()
    local_search = Averager()
    local_bid = Averager()
    local_queue = queue.Queue()
    
    # Background thread to sync fast local stats to the lock-free shared multiprocessing arrays
    def sync_loop():
        while not stop_event.is_set():
            shared_counter[worker_id] = local_counter.get()
            
            gt, gs, ga = local_get.get_raw_stats()
            shared_get[worker_id*3 + 0] = gt
            shared_get[worker_id*3 + 1] = gs
            shared_get[worker_id*3 + 2] = ga
            
            st, ss, sa = local_search.get_raw_stats()
            shared_search[worker_id*3 + 0] = st
            shared_search[worker_id*3 + 1] = ss
            shared_search[worker_id*3 + 2] = sa
            
            bt, bs, ba = local_bid.get_raw_stats()
            shared_bid[worker_id*3 + 0] = bt
            shared_bid[worker_id*3 + 1] = bs
            shared_bid[worker_id*3 + 2] = ba
            
            time.sleep(0.1)
            
    threading.Thread(target=sync_loop, daemon=True).start()

    clients = []
    for i in range(num_getters):
        client = GetterClient(target, env_type, all_items, local_queue, local_counter, local_get, local_search, stop_event)
        client.start()
        clients.append(client)
        
    for i in range(num_bidders):
        client = BidderClient(target, env_type, bidding_items, f"bidder-{os.getpid()}-{i}", local_queue, local_counter, local_bid, stop_event)
        client.start()
        clients.append(client)
        
    stop_event.wait()
    
    for client in clients:
        client.join(timeout=1.0)


class MultiProcessAveragerProxy:
    def __init__(self, shared_array, num_processes):
        self.shared_array = shared_array
        self.num_processes = num_processes
        
    def get_avg(self):
        total = sum(self.shared_array[i*3 + 0] for i in range(self.num_processes))
        success = sum(self.shared_array[i*3 + 1] for i in range(self.num_processes))
        return (total / success) if success > 0 else 0.0
        
    def get_success_rate(self):
        success = sum(self.shared_array[i*3 + 1] for i in range(self.num_processes))
        attempt = sum(self.shared_array[i*3 + 2] for i in range(self.num_processes))
        return (success / attempt) * 100.0 if attempt > 0 else 0.0

class MultiProcessCounterProxy:
    def __init__(self, shared_array):
        self.shared_array = shared_array
        
    def get(self):
        return sum(self.shared_array)

class WorkloadManager:
    def __init__(self, wrapper, bidding_items, all_items):
        self.target = getattr(wrapper, 'target', "localhost:50051")
        self.env_type = getattr(wrapper, 'env_type', "k8s")
        self.bidding_items = bidding_items
        self.all_items = all_items
        self.processes = []
        self.stop_event = None

    def start(self, num_getters=10, num_bidders=10, num_processes=10):
        self.num_processes = num_processes
        
        # Lock-free shared memory arrays for cross-process communication
        self.shared_counter = multiprocessing.Array(ctypes.c_longlong, num_processes)
        # Averagers need 3 values per process: [total_time, success_count, attempt_count]
        self.shared_get = multiprocessing.Array(ctypes.c_double, num_processes * 3)
        self.shared_search = multiprocessing.Array(ctypes.c_double, num_processes * 3)
        self.shared_bid = multiprocessing.Array(ctypes.c_double, num_processes * 3)
        
        # Proxies for simulate_load.py dashboard
        self.counter = MultiProcessCounterProxy(self.shared_counter)
        self.get_averager = MultiProcessAveragerProxy(self.shared_get, num_processes)
        self.search_averager = MultiProcessAveragerProxy(self.shared_search, num_processes)
        self.bid_averager = MultiProcessAveragerProxy(self.shared_bid, num_processes)

        self.stop_event = multiprocessing.Event()
        self.processes = []
        
        getters_per_proc = num_getters // num_processes
        bidders_per_proc = num_bidders // num_processes
        
        for i in range(num_processes):
            extra_get = (num_getters % num_processes) if i == 0 else 0
            extra_bid = (num_bidders % num_processes) if i == 0 else 0
            
            p = multiprocessing.Process(
                target=run_worker_process,
                args=(
                    i, self.target, self.env_type, self.all_items, self.bidding_items,
                    getters_per_proc + extra_get,
                    bidders_per_proc + extra_bid,
                    self.shared_counter, self.shared_get, self.shared_search, self.shared_bid,
                    self.stop_event
                )
            )
            p.start()
            self.processes.append(p)

    def stop(self):
        if self.stop_event:
            self.stop_event.set()
        for p in self.processes:
            p.join(timeout=2.0)
            if p.is_alive():
                p.terminate()
        self.processes.clear()
