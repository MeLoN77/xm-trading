import pytest
import requests
from tests.constants_for_test import BASE_URL


@pytest.mark.api
def test_create_order():
    order_data = {"details": "Buy 10 ounces of gold"}
    response = requests.post(f"{BASE_URL}/orders", json=order_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["order_id"] > 0
    assert response_data["status"] == "PENDING"


@pytest.mark.api
def test_get_order():
    order_data = {"details": "Buy 10 ounces of gold"}
    create_response = requests.post(f"{BASE_URL}/orders", json=order_data)
    order_id = create_response.json()["order_id"]

    response = requests.get(f"{BASE_URL}/orders/{order_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == order_id
    assert response_data["details"] == "Buy 10 ounces of gold"
    assert response_data["status"] == "PENDING"


@pytest.mark.api
def test_get_all_orders():
    response = requests.get(f"{BASE_URL}/orders")
    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, dict)


@pytest.mark.api
def test_update_order():
    order_data = {"details": "Buy 10 ounces of gold"}
    create_response = requests.post(f"{BASE_URL}/orders", json=order_data)
    order_id = create_response.json()["order_id"]
    update_data = {"status": "EXECUTED"}
    response = requests.put(f"{BASE_URL}/orders/{order_id}", json=update_data)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["order_id"] == order_id
    assert response_data["status"] == "EXECUTED"

    get_response = requests.get(f"{BASE_URL}/orders/{order_id}")
    get_response_data = get_response.json()
    assert get_response_data["status"] == "EXECUTED"


@pytest.mark.api
def test_delete_order():
    order_data = {"details": "Buy 10 ounces of gold"}
    create_response = requests.post(f"{BASE_URL}/orders", json=order_data)
    order_id = create_response.json()["order_id"]

    response = requests.delete(f"{BASE_URL}/orders/{order_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["order_id"] == order_id
    assert response_data["status"] == "DELETED"

    get_response = requests.get(f"{BASE_URL}/orders/{order_id}")
    assert get_response.status_code == 404


@pytest.mark.api
def test_clean_up():
    response = requests.get(f"{BASE_URL}/orders")
    assert response.status_code == 200
    response_data = response.json()
    for _order_id in response_data.items():
        _id = _order_id[1]['id']
        response = requests.delete(f"{BASE_URL}/orders/{_id}")
        assert response.status_code == 200
