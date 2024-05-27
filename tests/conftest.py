import pytest
from trade_xm_app.database import orders_db


@pytest.fixture(autouse=True)
def clear_orders():
    """
    Clear all orders before each test run
    :return:
    """
    orders_db.clear()
    global next_order_id
    next_order_id = 1
    yield
