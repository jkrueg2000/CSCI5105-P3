import os
from concurrent import futures
import threading

import grpc
from grpc_health.v1 import health, health_pb2, health_pb2_grpc
import pandas as pd
import pickle

import market_pb2
import market_pb2_grpc
import logging
from utils.logging_config import configure_logging

# initialize logging (idempotent)
configure_logging()
logger = logging.getLogger(__name__)

POD_NAME = os.environ.get("POD_NAME", "storage")
PORT = os.environ.get("PORT", "50052")

# Use a pandas DataFrame for item storage. This is an in-memory DataFrame
# representing the storage layer; in a production deployment this would be
# backed by a durable, replicated store.
DF_COLUMNS = [
    "item_id",
    "seller_id",
    "title",
    "category",
    "description",
    "starting_price",
    "current_price",
    "quantity",
    "status",
    "version",
]

DATA_DF = pd.DataFrame(columns=DF_COLUMNS).set_index("item_id")


class RWLock:
    """Read-write lock: multiple concurrent readers, exclusive writers.
    
    Uses threading primitives so it works with the multithreaded gRPC server.
    """
    def __init__(self):
        self._readers = 0
        self._lock = threading.Lock()        # protects _readers counter
        self._write_lock = threading.Lock()  # held by writers; readers block on it when first reader arrives

    class _ReaderCtx:
        def __init__(self, rwlock):
            self._rw = rwlock
        def __enter__(self):
            with self._rw._lock:
                self._rw._readers += 1
                if self._rw._readers == 1:
                    # First reader blocks writers
                    self._rw._write_lock.acquire()
        def __exit__(self, *exc):
            with self._rw._lock:
                self._rw._readers -= 1
                if self._rw._readers == 0:
                    # Last reader unblocks writers
                    self._rw._write_lock.release()

    class _WriterCtx:
        def __init__(self, rwlock):
            self._rw = rwlock
        def __enter__(self):
            self._rw._write_lock.acquire()
        def __exit__(self, *exc):
            self._rw._write_lock.release()

    def read_lock(self):
        return self._ReaderCtx(self)

    def write_lock(self):
        return self._WriterCtx(self)


DATA_LOCK = RWLock()


def _row_to_item(item_id, row) -> market_pb2.MarketplaceItem:
    item = market_pb2.MarketplaceItem()
    item.item_id = item_id
    item.seller_id = str(row.get("seller_id", ""))
    item.title = str(row.get("title", ""))
    item.category = str(row.get("category", ""))
    item.description = str(row.get("description", ""))
    item.starting_price = float(row.get("starting_price", 0.0) or 0.0)
    item.current_price = float(row.get("current_price", 0.0) or 0.0)
    item.quantity = int(row.get("quantity", 0) or 0)
    item.status = str(row.get("status", ""))
    item.version = int(row.get("version", 0) or 0)
    return item


class StorageService(market_pb2_grpc.StorageServiceServicer):
    def GetBackup(self, request, context):
        with DATA_LOCK.read_lock():
            data = pickle.dumps(DATA_DF)
        return market_pb2.BackupResponse(data=data)

    def CreateItem(self, request, context):
        if not request.is_replica_write:
            try:
                controller_target = os.environ.get("CONTROLLER_ADDR", "controller:50050")
                with grpc.insecure_channel(controller_target) as channel:
                    stub = market_pb2_grpc.ControllerServiceStub(channel)
                    resp = stub.CreateItemBackup(request, timeout=5)
                    if not resp.success:
                        return resp
            except Exception as e:
                return market_pb2.ActionResponse(success=False, message=f"controller err: {e}", new_version=0)
                
        item = request.item
        with DATA_LOCK.write_lock():
            if item.item_id in DATA_DF.index:
                existing = DATA_DF.loc[item.item_id]
                return market_pb2.ActionResponse(success=False, message="item exists", new_version=int(existing.get("version", 0) or 0))
            version = int(item.version or 0) or 1
            row = {
                "seller_id": item.seller_id,
                "title": item.title,
                "category": item.category,
                "description": item.description,
                "starting_price": float(item.starting_price or 0.0),
                "current_price": float(item.current_price or item.starting_price or 0.0),
                "quantity": int(item.quantity or 0),
                "status": item.status,
                "version": version,
            }
            DATA_DF.loc[item.item_id] = row
        logger.info("%s CreateItem %s", POD_NAME, item.item_id)
        return market_pb2.ActionResponse(success=True, message="created", new_version=version)

    def GetItem(self, request, context):
        item_id = request.item_id
        with DATA_LOCK.read_lock():
            if item_id not in DATA_DF.index:
                return market_pb2.MarketplaceItem()
            row = DATA_DF.loc[item_id]
            return _row_to_item(item_id, row)

    def SearchItems(self, request, context):
        q = (request.query or "").lower()
        cat = (request.category or "").lower()
        results = []
        with DATA_LOCK.read_lock():
            df = DATA_DF.copy()
        if q:
            mask = df["title"].fillna("").str.lower().str.contains(q) | df["description"].fillna("").str.lower().str.contains(q)
            df = df[mask]
        if cat:
            mask = df["category"].fillna("").str.lower() == cat
            df = df[mask]
        for item_id, row in df.iterrows():
            results.append(_row_to_item(item_id, row))
        return market_pb2.SearchResponse(items=results)

    def UpdateItem(self, request, context):
        if not request.is_replica_write:
            try:
                controller_target = os.environ.get("CONTROLLER_ADDR", "controller:50050")
                with grpc.insecure_channel(controller_target) as channel:
                    stub = market_pb2_grpc.ControllerServiceStub(channel)
                    resp = stub.UpdateBackups(request, timeout=5)
                    if not resp.success:
                        return resp
            except Exception as e:
                return market_pb2.ActionResponse(success=False, message=f"controller err: {e}", new_version=0)

        item_id = request.item_id
        with DATA_LOCK.write_lock():
            if item_id not in DATA_DF.index:
                return market_pb2.ActionResponse(success=False, message="not found", new_version=0)
            row = DATA_DF.loc[item_id].to_dict()
            # optional checks
            try:
                has_desc = request.HasField('description')
            except Exception:
                has_desc = bool(request.description)
            try:
                has_qty = request.HasField('quantity')
            except Exception:
                has_qty = request.quantity != 0
            try:
                has_status = request.HasField('status')
            except Exception:
                has_status = bool(request.status)
            current_version = int(row.get("version", 0) or 0)
            if request.expected_version and request.expected_version != current_version:
                return market_pb2.ActionResponse(success=False, message="version mismatch", new_version=current_version)
            if has_desc:
                row["description"] = request.description
            if has_qty:
                row["quantity"] = int(request.quantity)
            if has_status:
                row["status"] = request.status
            row["version"] = current_version + 1
            DATA_DF.loc[item_id] = row
            new_version = row["version"]
        logger.info("%s UpdateItem %s -> v%s", POD_NAME, item_id, new_version)
        return market_pb2.ActionResponse(success=True, message="updated", new_version=new_version)

    def PlaceBid(self, request, context):
        if not request.is_replica_write:
            try:
                controller_target = os.environ.get("CONTROLLER_ADDR", "controller:50050")
                with grpc.insecure_channel(controller_target) as channel:
                    stub = market_pb2_grpc.ControllerServiceStub(channel)
                    resp = stub.BidUpdateBackups(request, timeout=5)
                    if not resp.success:
                        return resp
            except Exception as e:
                return market_pb2.ActionResponse(success=False, message=f"controller err: {e}", new_version=0)

        item_id = request.item_id
        with DATA_LOCK.write_lock():
            if item_id not in DATA_DF.index:
                return market_pb2.ActionResponse(success=False, message="not found", new_version=0)
            row = DATA_DF.loc[item_id].to_dict()
            status = str(row.get("status", ""))
            current_price = float(row.get("current_price", 0.0) or 0.0)
            starting_price = float(row.get("starting_price", 0.0) or 0.0)
            version = int(row.get("version", 0) or 0)
            if status != "AUCTION_ACTIVE":
                return market_pb2.ActionResponse(success=False, message="auction not active", new_version=version)
            min_price = current_price or starting_price
            if request.bid_amount <= min_price:
                return market_pb2.ActionResponse(success=False, message="bid too low", new_version=version)
            row["current_price"] = float(request.bid_amount)
            row["version"] = version + 1
            DATA_DF.loc[item_id] = row
            new_version = row["version"]
        logger.info("%s PlaceBid %s bid=%s by %s", POD_NAME, item_id, request.bid_amount, request.bidder_id)
        return market_pb2.ActionResponse(success=True, message="bid accepted", new_version=new_version)

    def AuctionPoll(self, request, context):
        item_id = request.item_id
        with DATA_LOCK.read_lock():
            if item_id not in DATA_DF.index:
                return market_pb2.AuctionEvent(type=market_pb2.AuctionEvent.STATUS_CHANGE, item_snapshot=market_pb2.MarketplaceItem(), event_description="not found")
            row = DATA_DF.loc[item_id]
            item = _row_to_item(item_id, row)
            return market_pb2.AuctionEvent(type=market_pb2.AuctionEvent.STATUS_CHANGE, item_snapshot=item, event_description="polled")


def serve():
    # Sync from controller
    controller_target = os.environ.get("CONTROLLER_ADDR", "controller:50050")
    try:
        with grpc.insecure_channel(controller_target) as channel:
            stub = market_pb2_grpc.ControllerServiceStub(channel)
            resp = stub.GetBackup(market_pb2.BackupRequest(), timeout=5)
            if resp.data:
                global DATA_DF
                with DATA_LOCK.write_lock():
                    DATA_DF = pickle.loads(resp.data)
                logger.info("Successfully loaded backup from controller.")
    except Exception as e:
        logger.warning(f"Could not load backup from controller: {e}")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_StorageServiceServicer_to_server(StorageService(), server)

    # Health servicer for Kubernetes gRPC probes
    health_servicer = health.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
    # mark overall server as SERVING
    health_servicer.set("", health_pb2.HealthCheckResponse.SERVING)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    logger.info("storage %s listening on %s", POD_NAME, PORT)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
