import requests
import pytest

@pytest.mark.parametrize("price", [0, -100])
def test_add_dish_invalid_price(base_url, restaurant_id, price):
    payload = {
        "name": "Invalid",
        "type": "Veg",
        "price": price,
        "available_time": "10AM-10PM",
        "image": "img.jpg"
    }
    response = requests.post(
        f"{base_url}/api/v1/restaurants/{restaurant_id}/dishes",
        json=payload
    )
    assert response.status_code == 400


def test_update_dish(base_url, dish_id):
    payload = {"price": 250}
    response = requests.put(
        f"{base_url}/api/v1/dishes/{dish_id}",
        json=payload
    )
    assert response.status_code == 200


def test_update_dish_status(base_url, dish_id):
    payload = {"enabled": False}
    response = requests.put(
        f"{base_url}/api/v1/dishes/{dish_id}/status",
        json=payload
    )
    assert response.status_code == 200


def test_delete_dish(base_url, dish_id):
    response = requests.delete(
        f"{base_url}/api/v1/dishes/{dish_id}"
    )
    assert response.status_code == 200
