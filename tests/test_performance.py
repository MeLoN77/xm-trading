import pytest
import requests
import time
from tests.constants_for_test import BASE_URL


@pytest.mark.performance
def test_performance():
    order_data = {"details": "Buy 1 ounce of silver 100 times"}
    start_time = time.time()
    for _ in range(100):
        response = requests.post(f"{BASE_URL}/orders", json=order_data)
        assert response.status_code == 200
    end_time = time.time()
    duration = end_time - start_time
    response = requests.get(f"{BASE_URL}/orders")
    assert duration <= 1.5
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) >= 100
