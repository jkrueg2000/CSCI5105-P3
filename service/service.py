import os
import asyncio

import grpc

import kv_pb2
import kv_pb2_grpc

POD_NAME = os.environ.get("POD_NAME", "SERVICE")
PORT = os.environ.get("PORT", "50051")

# Storage configuration (external storage service via gRPC)
STORAGE_PORT = os.environ.get("STORAGE_PORT", "50052")
# Use a single replicated storage service; service does not shard or replicate
STORAGE_TARGET = f"storage:{STORAGE_PORT}"

INDEX_KEY = "marketplace:items_index"

# Auction subscribers (kept in-memory for streaming updates)
ITEMS_LOCK = asyncio.Lock()
AUCTION_SUBSCRIBERS = {}  # item_id -> list of asyncio.Queue


class MarketplaceFrontend(kv_pb2_grpc.MarketplaceServiceServicer):
    async def CreateItem(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = kv_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.CreateItem(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return kv_pb2.ActionResponse(success=False, message=str(e), new_version=0)

    async def GetItem(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = kv_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.GetItem(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return kv_pb2.MarketplaceItem()

    async def SearchItems(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = kv_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.SearchItems(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return kv_pb2.SearchResponse(items=[])

    async def UpdateItem(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = kv_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.UpdateItem(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return kv_pb2.ActionResponse(success=False, message=str(e), new_version=0)

    async def PlaceBid(self, request, context):
        target = STORAGE_TARGET
        async with grpc.aio.insecure_channel(target) as channel:
            stub = kv_pb2_grpc.StorageServiceStub(channel)
            try:
                resp = await stub.PlaceBid(request)
                return resp
            except grpc.aio.AioRpcError as e:
                context.set_code(e.code())
                context.set_details(e.details())
                return kv_pb2.ActionResponse(success=False, message=str(e), new_version=0)

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

    def _notify(self, item_id, event):
        # sync helper called from async methods; queues are asyncio.Queue
        subs = list(AUCTION_SUBSCRIBERS.get(item_id, []))
        for q in subs:
            try:
                q.put_nowait(event)
            except Exception:
                pass
 

async def serve():
    server = grpc.aio.server()
    kv_pb2_grpc.add_MarketplaceServiceServicer_to_server(MarketplaceFrontend(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    await server.start()
    print(f"frontend {POD_NAME} listening on {PORT}", flush=True)
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
