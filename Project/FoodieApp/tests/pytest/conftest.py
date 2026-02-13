import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def restaurant_id(base_url):
    payload = {
        "name": "Test Restaurant",
        "category": "Veg",
        "location": "Delhi",
        "images": ["img1.jpg"],
        "contact": "9999999999"
    }
    response = requests.post(f"{base_url}/api/v1/restaurants", json=payload)
    assert response.status_code == 201
    return response.json()["id"]


@pytest.fixture(scope="session")
def user_id(base_url):
    payload = {
        "name": "Test User",
        "email": "testuser@mail.com",
        "password": "123456"
    }
    response = requests.post(f"{base_url}/api/v1/users/register", json=payload)
    assert response.status_code == 201
    return response.json()["id"]


@pytest.fixture(scope="session")
def dish_id(base_url, restaurant_id):
    payload = {
        "name": "Paneer",
        "type": "Veg",
        "price": 200,
        "available_time": "10AM-10PM",
        "image": "paneer.jpg"
    }
    response = requests.post(
        f"{base_url}/api/v1/restaurants/{restaurant_id}/dishes",
        json=payload
    )
    assert response.status_code == 201
    return response.json()["id"]


@pytest.fixture(scope="session")
def order_id(base_url, user_id, restaurant_id, dish_id):
    payload = {
        "user_id": user_id,
        "restaurant_id": restaurant_id,
        "dishes": [dish_id]
    }
    response = requests.post(f"{base_url}/api/v1/orders", json=payload)
    assert response.status_code == 201
    return response.json()["id"]
