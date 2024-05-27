from fastapi import WebSocket, WebSocketDisconnect
from typing import List
from trade_xm_app.models import Order, OrderStatusEnum, OrderCreate
from trade_xm_app.database import add_order, get_order, update_order_status, delete_order, get_all_orders

clients: List[WebSocket] = []


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            command, *params = data.split(":", 1)
            if command == "CREATE_ORDER":
                details = params[0] if params else ""
                order = OrderCreate(details=details)
                order_id = add_order(Order(id=0, details=order.details, status=OrderStatusEnum.PENDING))
                response = f"ORDER_CREATED:{order_id}:PENDING"
                await websocket.send_text(response)
            elif command == "UPDATE_STATUS":
                order_id, status = params[0].split(",")
                order_id = int(order_id)
                if status not in OrderStatusEnum.__members__:
                    await websocket.send_text(f"INVALID_STATUS:{status}")
                else:
                    update_order_status(order_id, OrderStatusEnum[status])
                    response = f"STATUS_UPDATED:{order_id}:{status}"
                    await websocket.send_text(response)
            elif command == "GET_ORDER":
                order_id = int(params[0])
                order = get_order(order_id)
                response = f"ORDER:{order.id}:{order.details}:{order.status}"
                await websocket.send_text(response)
            elif command == "DELETE_ORDER":
                order_id = int(params[0])
                await delete_order(order_id)
                response = f"ORDER_DELETED:{order_id}"
                await websocket.send_text(response)
            elif command == "GET_ALL_ORDERS":
                all_orders = get_all_orders()
                response = "ALL_ORDERS:" + ";".join(
                    [f"{order.id}:{order.details}:{order.status}" for order in all_orders.values()])
                await websocket.send_text(response)
            else:
                await websocket.send_text(f"UNKNOWN_COMMAND:{data}")
    except WebSocketDisconnect:
        clients.remove(websocket)
