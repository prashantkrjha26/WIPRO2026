import requests

def test_view_orders_by_restaurant(base_url, restaurant_id):
    response = requests.get(
        f"{base_url}/api/v1/restaurants/{restaurant_id}/orders"
    )
    assert response.status_code == 200


def test_view_orders_by_user(base_url, user_id):
    response = requests.get(
        f"{base_url}/api/v1/users/{user_id}/orders"
    )
    assert response.status_code == 200
