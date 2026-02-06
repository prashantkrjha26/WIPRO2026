import pytest
import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/patients"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def headers():
    return {
        "Content-Type": "application/json"
    }


@pytest.fixture
def create_patient(base_url, headers):
    """
    Creates a patient before test execution
    and returns created patient data
    """
    payload = {
        "name": "Test Patient",
        "age": 40,
        "gender": "Male",
        "contact": "9998887776",
        "disease": "Cold",
        "doctor": "Dr. Test"
    }

    response = requests.post(
        base_url,
        headers=headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 201
    return response.json()["data"]
