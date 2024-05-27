from typing import Dict
from trade_xm_app.models import Order, OrderStatusEnum

orders_db: Dict[int, Order] = {}
next_order_id = 1


def add_order(order: Order) -> int:
    """
    Add new order into DB
    :param (obj) order: Order objet
    :return:
    """
    global next_order_id
    order.id = next_order_id
    order.status = OrderStatusEnum.PENDING
    orders_db[next_order_id] = order
    next_order_id += 1
    return order.id


def get_order(order_id: int) -> Order:
    """
    Get 1 order by its ID number
    :param (int) order_id: Order ID
    :return:
    """
    return orders_db.get(order_id)


def update_order_status(order_id: int, status: OrderStatusEnum):
    """
    Update order status
    :param (int) order_id: 2
    :param (obj) status: OrderStatusEnum object
    :return:
    """
    if order_id in orders_db:
        orders_db[order_id].status = status


async def delete_order(order_id: int) -> bool:
    """
    Remove order by ID
    :param (int) order_id: 3
    :return:
    """
    if order_id in orders_db:
        del orders_db[order_id]
        return True

    return False


def get_all_orders() -> Dict[int, Order]:
    """
    Get all orders
    :return:
    """
    return orders_db
