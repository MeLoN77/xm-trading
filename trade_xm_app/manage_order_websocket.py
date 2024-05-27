import asyncio
import websockets


async def manage_order():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("CREATE_ORDER:Order details")
        response = await websocket.recv()
        _, order_id, status = response.split(":")
        order_id = int(order_id)
        await websocket.send(f"UPDATE_STATUS:{order_id},EXECUTED")
        await websocket.recv()
        await websocket.send(f"UPDATE_STATUS:{order_id},CANCELLED")
        await websocket.recv()


asyncio.get_event_loop().run_until_complete(manage_order())
