import requests

def test_duplicate_user(base_url, user_id):
    payload = {
        "name": "Test User",
        "email": "testuser@mail.com",
        "password": "123456"
    }
    response = requests.post(
        f"{base_url}/api/v1/users/register",
        json=payload
    )
    assert response.status_code == 409


def test_give_rating(base_url, order_id):
    payload = {
        "order_id": order_id,
        "rating": 5,
        "comment": "Excellent"
    }
    response = requests.post(
        f"{base_url}/api/v1/ratings",
        json=payload
    )
    assert response.status_code == 201
