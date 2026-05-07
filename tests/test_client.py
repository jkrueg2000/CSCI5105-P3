#!/usr/bin/env python3
"""Simple integration test: Create an item via the service and read it back.
Exits 0 on success, non-zero on failure.
"""
import os
import sys
import uuid
import time
import logging

import grpc

import market_pb2
import market_pb2_grpc


def wait_for_service(target, timeout=30, interval=1):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with grpc.insecure_channel(target) as ch:
                stub = market_pb2_grpc.MarketplaceServiceStub(ch)
                # cheap call to verify server is reachable
                _ = stub.GetItem(market_pb2.GetItemRequest(item_id="__health_check__"), timeout=2)
                return True
        except Exception:
            time.sleep(interval)
    return False


def main():
    logging.basicConfig(level=logging.INFO)
    target = os.environ.get("SERVICE_TARGET", "localhost:50051")
    logging.info("Service target: %s", target)

    if not wait_for_service(target, timeout=30):
        logging.error("Service did not become ready within timeout")
        return 2

    stub = market_pb2_grpc.MarketplaceServiceStub(grpc.insecure_channel(target))

    item_id = f"test-{uuid.uuid4().hex[:8]}"
    item = market_pb2.MarketplaceItem(
        item_id=item_id,
        seller_id="tester",
        title="Integration Test Item",
        category="test",
        description="Created by integration test",
        starting_price=1.0,
        current_price=1.0,
        quantity=1,
        status="AVAILABLE",
        version=1,
    )

    create_req = market_pb2.CreateItemRequest(item=item)
    logging.info("Creating item %s", item_id)
    try:
        resp = stub.CreateItem(create_req, timeout=5)
    except grpc.RpcError:
        logging.exception("CreateItem RPC failed")
        return 3

    logging.info("CreateItem response: success=%s message=%s new_version=%s", resp.success, resp.message, resp.new_version)
    if not getattr(resp, "success", False):
        logging.error("CreateItem reported failure")
        return 4

    # fetch it back
    try:
        got = stub.GetItem(market_pb2.GetItemRequest(item_id=item_id), timeout=5)
    except grpc.RpcError:
        logging.exception("GetItem RPC failed")
        return 5

    logging.info("GetItem returned item_id=%s title=%s", got.item_id, got.title)
    if got.item_id != item_id:
        logging.error("GetItem returned wrong item id %s != %s", got.item_id, item_id)
        return 6

    print("GET-PASS")

    # 4. Search items
    try:
        search_req = market_pb2.SearchRequest(query="Integration")
        search_resp = stub.SearchItems(search_req, timeout=5)
        if not any(i.item_id == item_id for i in search_resp.items):
            logging.error("SearchItems didn't find the item")
            return 7
    except grpc.RpcError:
        logging.exception("SearchItems RPC failed")
        return 8
    print("SEARCH-PASS")

    # 5. Update item
    try:
        update_req = market_pb2.UpdateItemRequest(
            item_id=item_id,
            description="Updated description",
            status="AUCTION_ACTIVE"
        )
        update_resp = stub.UpdateItem(update_req, timeout=5)
        if not getattr(update_resp, "success", False):
            logging.error("UpdateItem reported failure")
            return 9
    except grpc.RpcError:
        logging.exception("UpdateItem RPC failed")
        return 10
    print("UPDATE-PASS")

    # 6. Place bid
    try:
        bid_req = market_pb2.BidRequest(
            item_id=item_id,
            bidder_id="bidder-123",
            bid_amount=10.0
        )
        bid_resp = stub.PlaceBid(bid_req, timeout=5)
        if not getattr(bid_resp, "success", False):
            logging.error("PlaceBid reported failure: %s", bid_resp.message)
            return 11
    except grpc.RpcError:
        logging.exception("PlaceBid RPC failed")
        return 12
    print("BID-PASS")

    print("ALL TESTS PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
