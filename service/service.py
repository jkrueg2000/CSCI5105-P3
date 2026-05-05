import os
import asyncio

import grpc

import market_pb2
import market_pb2_grpc

POD_NAME = os.environ.get("POD_NAME", "SERVICE")
PORT = os.environ.get("PORT", "50051")

# Storage configuration (external storage service via gRPC)
STORAGE_PORT = os.environ.get("STORAGE_PORT", "50052")
# Use a single replicated storage service; service does not shard or replicate
STORAGE_TARGET = f"storage:{STORAGE_PORT}"

INDEX_KEY = "marketplace:items_index"

class ItemAuctionTracker:
    def __init__(self, item_id):
        self.item_id = item_id
        self.subscribers = {} #sub id -> asyncio.Queue for updates
        self.lock = asyncio.Lock()
        self.item = None  # Cache of the current item state
        self.bids = asyncio.Queue()  # Queue for incoming bids to this item
        self.polling_task = None
        self.bids_task = None


    async def startup(self):
        async with grpc.aio.insecure_channel(STORAGE_TARGET) as channel:
            stub = kv_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.GetItem(kv_pb2.GetItemRequest(item_id=self.item_id))
                if resp.item:
                    # If item exists, start polling for updates
                    self.item = resp.item
                    asyncio.create_task(self.poll())
            except grpc.aio.AioRpcError as e:
                print(f"Error initializing tracker for item {self.item_id}: {e}")

    async def poll(self):
        async with grpc.aio.insecure_channel(STORAGE_TARGET) as channel:
            stub = kv_pb2_grpc.StorageServiceStub(channel)
            while True:
                await asyncio.sleep(5)
                try:
                    resp = await stub.GetItem(kv_pb2.GetItemRequest(item_id=self.item_id))
                    if not resp.item:
                        # Item was deleted, notify subscribers and exit
                        await self._notify_subscribers(kv_pb2.AuctionEvent(
                            item_id=self.item_id,
                            event_type=kv_pb2.AuctionEvent.DELETED
                        ))
                        break
                    
                    if resp.item.version != self.item.version:
                        # Item was updated, notify subscribers
                        if resp.item.current_price != self.item.current_price:
                            await self._notify_subscribers(kv_pb2.AuctionEvent(
                                item_id=self.item_id,
                                event_type=kv_pb2.AuctionEvent.NEW_BID,
                                item=resp.item
                            ))
                        else:
                            await self._notify_subscribers(kv_pb2.AuctionEvent(
                                item_id=self.item_id,
                                event_type=kv_pb2.AuctionEvent.UPDATED,
                                item=self.item
                            ))
                        self.item = resp.item

                except grpc.aio.AioRpcError as e:
                    print(f"Error polling item {self.item_id}: {e}")
                await asyncio.sleep(5)  # Poll every second

    async def _notify_subscribers(self, event):
        async with self.lock:
            subs = list(self.subscribers.get(self.item_id, []))
        for q in subs:
            try:
                await q.put(event)
            except Exception:
                pass

    async def subscribe(self):
        q = asyncio.Queue()
        async with self.lock:
            sub_id = max(self.subscribers.keys(), default=0) + 1
            self.subscribers[sub_id] = q
        return sub_id, q
    
    async def unsubscribe(self, sub_id):
        async with self.lock:
            if sub_id in self.subscribers:
                del self.subscribers[sub_id]
    
    def __delete__(self):
        for q in self.subscribers.get(self.item_id, []):
            try:
                q.shutdown()  # Signal to subscribers that this tracker is being deleted
            except Exception:
                pass

class MarketplaceService(market_pb2_grpc.MarketplaceServiceServicer):
    def __init__(self):
        super().__init__()
        self.lock = asyncio.Lock()
        self.active_trackers = {}  # item_id -> auction tracker

    async def _get_or_create_tracker(self, item_id):
        async with self.lock:
            if item_id not in self.active_trackers:
                tracker = ItemAuctionTracker(item_id)
                self.active_trackers[item_id] = tracker
                asyncio.create_task(tracker._startup())
            return self.active_trackers[item_id]

    async def CreateItem(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = market_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.CreateItem(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return market_pb2.ActionResponse(success=False, message=str(e), new_version=0)

    async def GetItem(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = market_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.GetItem(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return market_pb2.MarketplaceItem()

    async def SearchItems(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = market_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.SearchItems(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return market_pb2.SearchResponse(items=[])

    async def UpdateItem(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = market_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.UpdateItem(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return market_pb2.ActionResponse(success=False, message=str(e), new_version=0)

    async def PlaceBid(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = market_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.PlaceBid(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return market_pb2.ActionResponse(success=False, message=str(e), new_version=0)

    async def JoinAuction(self, request, context):
        item_id = request.item_id
        q = asyncio.Queue()
        async with ITEMS_LOCK:
            subs = AUCTION_SUBSCRIBERS.setdefault(item_id, [])
            subs.append(q)
        try:
            while True:
                evt = await q.get()
                yield evt
        finally:
            async with ITEMS_LOCK:
                subs = AUCTION_SUBSCRIBERS.get(item_id, [])
                if q in subs:
                    subs.remove(q)
 

async def serve():
    server = grpc.aio.server()
    market_pb2_grpc.add_MarketplaceServiceServicer_to_server(MarketplaceService(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    await server.start()
    print(f"frontend {POD_NAME} listening on {PORT}", flush=True)
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
