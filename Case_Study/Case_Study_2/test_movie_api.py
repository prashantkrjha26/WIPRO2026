import pytest
import requests
from Tools.scripts.fixdiv import report

# Base URL where the Flask API is running
BASE_URL = "http://127.0.0.1:5000"


# ---------- FIXTURE ----------
# Creates a movie before test and deletes it after test
@pytest.fixture
def test_movie():
    payload = {
        "id": 999,
        "movie_name": "Test Movie",
        "language": "English",
        "duration": "2h",
        "price": 100
    }

    # Setup: add movie
    requests.post(
        f"{BASE_URL}/api/movies",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    yield payload

    # Teardown: delete movie
    requests.delete(f"{BASE_URL}/api/movies/999")


# ---------- BASIC TESTS ----------

def test_home_page():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Welcome to Movie Ticket Booking" in response.text


def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_movie_by_id():
    response = requests.get(f"{BASE_URL}/api/movies/101")
    assert response.status_code == 200
    assert response.json()["movie_name"] == "Interstellar"


# ---------- CRUD USING FIXTURE ----------

def test_update_movie(test_movie):
    movie_id = test_movie["id"]

    response = requests.put(
        f"{BASE_URL}/api/movies/{movie_id}",
        json={"price": 150},
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 200
    assert response.json()["price"] == 150


def test_delete_movie(test_movie):
    movie_id = test_movie["id"]

    response = requests.delete(f"{BASE_URL}/api/movies/{movie_id}")
    assert response.status_code == 200
    assert "Movie deleted successfully" in response.json()["message"]


# ---------- BOOKING TESTS ----------

def test_book_tickets():
    payload = {
        "movie_id": 104,
        "seats": 3
    }

    response = requests.post(
        f"{BASE_URL}/api/bookings",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 201
    assert response.json()["total_price"] == 690


# ---------- PARAMETERIZED NEGATIVE TESTS ----------

@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"movie_id": 9999, "seats": 1}, 404),
        ({"movie_id": 101, "seats": 0}, 400),
        ({}, 400)
    ]
)
def test_booking_negative_cases(payload, expected_status):
    response = requests.post(
        f"{BASE_URL}/api/bookings",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == expected_status



# To Generate html report
# pytest --html=report.html --self-contained-html
