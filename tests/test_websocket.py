import pytest
import websockets
from tests.constants_for_test import WEB_SOCKET_URI


@pytest.mark.websocket
async def test_websocket_operations(clear_orders):
    
    async with websockets.connect(WEB_SOCKET_URI) as websocket:
        await websocket.send("CREATE_ORDER:Buy 10 ounces of gold")
        response = await websocket.recv()
        assert "ORDER_CREATED" in response

        _, order_id, status = response.split(":")
        order_id = int(order_id)
        assert status == "PENDING"

        await websocket.send(f"UPDATE_STATUS:{order_id},EXECUTED")
        response = await websocket.recv()
        assert f"STATUS_UPDATED:{order_id}:EXECUTED" == response

        await websocket.send(f"GET_ORDER:{order_id}")
        response = await websocket.recv()
        assert f"ORDER:{order_id}:Buy 10 ounces of gold:EXECUTED" == response

        await websocket.send(f"DELETE_ORDER:{order_id}")
        response = await websocket.recv()
        assert f"ORDER_DELETED:{order_id}" == response

        await websocket.send("GET_ALL_ORDERS")
        response = await websocket.recv()
        assert "ALL_ORDERS:" == response
