from fastapi import APIRouter, HTTPException
from trade_xm_app.database import (
    get_all_orders,
    add_order,
    update_order_status,
    delete_order,
    get_order
)
from trade_xm_app.models import (
    OrderCreate,
    OrderUpdate,
    Order,
    OrderStatusEnum
)

router = APIRouter()


@router.get("/orders")
async def read_orders():
    return get_all_orders()


@router.post("/orders")
async def create_order(order: OrderCreate):
    order_id = add_order(Order(id=0, details=order.details, status=OrderStatusEnum.PENDING))
    return {"order_id": order_id, "status": "PENDING"}


@router.put("/orders/{order_id}")
async def update_order(order_id: int, order_update: OrderUpdate):
    update_order_status(order_id, order_update.status)
    return {"order_id": order_id, "status": order_update.status}


@router.delete("/orders/{order_id}")
async def delete_order_endpoint(order_id: int):
    if await delete_order(order_id):
        return {"order_id": order_id, "status": "DELETED"}
    raise HTTPException(status_code=404, detail="Order not found")


@router.get("/orders/{order_id}")
async def read_order(order_id: int):
    order = get_order(order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")
