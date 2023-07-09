import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app=app)
token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhIiwiaWF0IjoxNjg0NjQ3OTI2LCJuYmYiOjE2ODQ2NDc5MjYsImp0aSI6ImQ3MTViM2IyLWFkZDQtNDAzMi05ZGQ1LTM3NDdhMjQ2MDJiMCIsImV4cCI6MTY4NDY0ODgyNiwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.Of7S6lL4WBRcdJA3T6iDXKVSG_bjYq_HVAWHLearkmU'


@pytest.mark.parametrize(
    "input_data, expected_status_code",
    [
        ({"username": "a", "password": 'a'}, 400),
        ({"username": "Item", "aasdsa": "sadsa"}, 400),

        # Add more test scenarios as needed
    ],
)
def test_create_user(input_data, expected_status_code):
    response = client.post("/users/", json=input_data)
    assert response.status_code == expected_status_code


@pytest.mark.parametrize("access_token", [token])
def test_api_with_token_and_json(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
                "title" : "sdfsdfsfsdf",
                "description" : "workshop",
                "start_time" : "1401/01/15T15:36:18",
                "end_time" : "1402/01/15T15:36:18",
                "Capacity" : 52,
                "items" : "some string"

            }
    response = client.post("/conferences/", json=data, headers=headers)
    assert response.status_code == 201
    # Add additional assertions as needed


@pytest.mark.parametrize("access_token", [token])
def test_api_with_token_and_jso(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
                "title" : "sdfsdfsfsdf",
                "description" : "workshop",
                "start_time" : "1401/01/15T15:36:18",
                "end_time" : "14s02/01/15T15:36:18",
                "Capacity" : 52,
                "items" : "some string"

            }
    response = client.post("/conferences/", json=data, headers=headers)
    assert response.status_code == 400
    # Add additional assertions as needed


@pytest.mark.parametrize(
    "input_data, expected_status_code",
    [
        ({"username": "aa", "password": "aa"}, 200),
        ({"username": "Item", "aasdsa": "sadsa"}, 400),

        # Add more test scenarios as needed
    ],
)
def test_login(input_data, expected_status_code):
    response = client.post("/login/", json=input_data)
    assert response.status_code == expected_status_code

@pytest.mark.parametrize("access_token", [token])
def Get_all_conferences(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    response = client.get("/conferences/", headers=headers)
    assert response.status_code == 200

@pytest.mark.parametrize("access_token", [token])
def test_Update_an_existing_conference(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
                "title" : "sdfsdfsfsdf",
                "description" : "workshop",
                "start_time" : "1401/01/15T15:36:18",
                "end_time" : "14s02/01/15T15:36:18",
                "Capacity" : 52,
                "items" : "some string"

            }
    response = client.post("/conferences/", json=data, headers=headers)
    assert response.status_code == 400
    # Add additional assertions as needed

@pytest.mark.parametrize("access_token", [token])
def test_Update_an_existing_conferene(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
                "title" : "sdfsdfsfsdf",
                "description" : "workshop",
                "start_time" : "1401/01/15T15:36:18",
                "end_time" : "14s02/01/15T15:36:18",
                "Capacity" : 52,
                "items" : "some string"

            }
    response = client.post("/conferences/65", json=data, headers=headers)
    assert response.status_code == 405
    # Add additional assertions as needed

