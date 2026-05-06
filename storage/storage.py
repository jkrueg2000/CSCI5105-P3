import os
from concurrent import futures
import threading

import grpc
import pandas as pd

import market_pb2
import market_pb2_grpc

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
DATA_LOCK = threading.Lock()


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
    def CreateItem(self, request, context):
        item = request.item
        with DATA_LOCK:
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
        print(f"{POD_NAME} CreateItem {item.item_id}", flush=True)
        return market_pb2.ActionResponse(success=True, message="created", new_version=version)

    def GetItem(self, request, context):
        item_id = request.item_id
        with DATA_LOCK:
            if item_id not in DATA_DF.index:
                return market_pb2.MarketplaceItem()
            row = DATA_DF.loc[item_id]
            return _row_to_item(item_id, row)

    def SearchItems(self, request, context):
        q = (request.query or "").lower()
        cat = (request.category or "").lower()
        results = []
        with DATA_LOCK:
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
        item_id = request.item_id
        with DATA_LOCK:
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
        print(f"{POD_NAME} UpdateItem {item_id} -> v{new_version}", flush=True)
        return market_pb2.ActionResponse(success=True, message="updated", new_version=new_version)

    def PlaceBid(self, request, context):
        item_id = request.item_id
        with DATA_LOCK:
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
        print(f"{POD_NAME} PlaceBid {item_id} bid={request.bid_amount} by {request.bidder_id}", flush=True)
        return market_pb2.ActionResponse(success=True, message="bid accepted", new_version=new_version)

    def AuctionPoll(self, request, context):
        item_id = request.item_id
        with DATA_LOCK:
            if item_id not in DATA_DF.index:
                return market_pb2.AuctionEvent(type=market_pb2.AuctionEvent.STATUS_CHANGE, item_snapshot=market_pb2.MarketplaceItem(), event_description="not found")
            row = DATA_DF.loc[item_id]
            item = _row_to_item(item_id, row)
            return market_pb2.AuctionEvent(type=market_pb2.AuctionEvent.STATUS_CHANGE, item_snapshot=item, event_description="polled")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_StorageServiceServicer_to_server(StorageService(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    print(f"storage {POD_NAME} listening on {PORT}", flush=True)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
