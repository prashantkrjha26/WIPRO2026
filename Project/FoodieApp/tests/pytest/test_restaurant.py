import requests
import pytest

def test_register_restaurant_negative(base_url):
    response = requests.post(f"{base_url}/api/v1/restaurants", json={})
    assert response.status_code == 400


def test_view_restaurant(base_url, restaurant_id):
    response = requests.get(f"{base_url}/api/v1/restaurants/{restaurant_id}")
    assert response.status_code == 200
    body = response.json()
    assert "id" in body
    assert "name" in body


def test_update_restaurant(base_url, restaurant_id):
    payload = {"location": "Mumbai"}
    response = requests.put(
        f"{base_url}/api/v1/restaurants/{restaurant_id}",
        json=payload
    )
    assert response.status_code == 200
    assert response.json()["location"] == "Mumbai"


def test_disable_restaurant(base_url, restaurant_id):
    response = requests.put(
        f"{base_url}/api/v1/restaurants/{restaurant_id}/disable"
    )
    assert response.status_code == 200


def test_search_restaurant(base_url):
    response = requests.get(
        f"{base_url}/api/v1/restaurants/search?name=Test"
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
