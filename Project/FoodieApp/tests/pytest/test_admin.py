import requests

def test_admin_approve(base_url, restaurant_id):
    response = requests.put(
        f"{base_url}/api/v1/admin/restaurants/{restaurant_id}/approve"
    )
    assert response.status_code == 200


def test_admin_disable(base_url, restaurant_id):
    response = requests.put(
        f"{base_url}/api/v1/admin/restaurants/{restaurant_id}/disable"
    )
    assert response.status_code == 200


def test_view_feedback(base_url):
    response = requests.get(
        f"{base_url}/api/v1/admin/feedback"
    )
    assert response.status_code == 200


def test_view_admin_orders(base_url):
    response = requests.get(
        f"{base_url}/api/v1/admin/orders"
    )
    assert response.status_code == 200
