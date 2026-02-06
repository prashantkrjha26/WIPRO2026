import pytest
import requests
import json


def test_register_patient(base_url, headers):
    payload = {
        "name": "Amit Kumar",
        "age": 32,
        "gender": "Male",
        "contact": "9123456789",
        "disease": "Cough",
        "doctor": "Dr. Sharma"
    }

    response = requests.post(
        base_url,
        headers=headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 201
    assert response.json()["status"] == "success"
    assert response.json()["data"]["name"] == "Amit Kumar"


def test_get_all_patients(base_url):
    response = requests.get(base_url)

    # API can return 200 (when patients exist) or 404 (when empty)
    assert response.status_code in [200, 404]


def test_get_patient_by_id(base_url, create_patient):
    patient_id = create_patient["id"]

    response = requests.get(f"{base_url}/{patient_id}")

    assert response.status_code == 200
    assert response.json()["data"]["id"] == patient_id


def test_update_patient(base_url, headers, create_patient):
    patient_id = create_patient["id"]

    payload = {
        "age": 45,
        "disease": "Migraine"
    }

    response = requests.put(
        f"{base_url}/{patient_id}",
        headers=headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 200
    assert response.json()["data"]["age"] == 45


@pytest.mark.parametrize(
    "payload",
    [
        {"age": 25, "gender": "Male", "contact": "9876543210"},
        {"name": "", "age": 25, "gender": "Male", "contact": "9876543210"},
        {"name": "Ravi", "age": -5, "gender": "Male", "contact": "9876543210"},
        {"name": "Ravi", "age": 25, "gender": "Male", "contact": "1234"},
    ]
)
def test_negative_register_patient(base_url, headers, payload):
    response = requests.post(
        base_url,
        headers=headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 400
    assert response.json()["status"] == "error"


@pytest.mark.skip(reason="Delete patient API not implemented yet")
def test_delete_patient():
    pass


@pytest.mark.xfail(reason="Known issue: API allows empty gender on update")
def test_update_patient_invalid_gender(base_url, headers, create_patient):
    patient_id = create_patient["id"]

    payload = {
        "gender": ""
    }

    response = requests.put(
        f"{base_url}/{patient_id}",
        headers=headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 400
