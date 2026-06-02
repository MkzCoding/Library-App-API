import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_member_login_success():
    response = client.post("/login/member", json = {"username":"testmember", "password":"testpassword"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == 'bearer'


def test_member_login_invalid_credentials():
    response = client.post("/login/member", json = {"username":"testmember", "password": "wrongpassword" })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid Credentials."

def test_member_login_not_found():
    response = client.post("/login/member", json = {"username":"wrongusername", "password": "wrongpassword" })
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found."


def test_librarian_login_success():
    response = client.post("/login/librarian", json = {"username":"thelibrarian", "password":"librarian123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == 'bearer'


def test_librarian_login_invalid_credentials():
    response = client.post("/login/librarian", json = {"username":"thelibrarian", "password": "wrongpassword" })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid Credentials."

def test_librarian_login_not_found():
    response = client.post("/login/librarian", json = {"username":"wrongusername", "password": "wrongpassword" })
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found."




