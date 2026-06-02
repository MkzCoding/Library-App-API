import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_member_member_conflict():
    response = client.post("/registration/registration", json= {"name":"testingmember", "email":"testing@test.com", "username":"testingmemberusername2","password":"testingpassword", "usertype":"member"})
    assert response.status_code == 200

    response = client.post("/registration/registration", json= {"name":"testingmember", "email":"testing@test.com", "username":"testingmemberusername","password":"testingpassword", "usertype":"member"})
    assert response.status_code == 409
    assert response.json()["detail"] == "User already exists."

def test_create_librarian_librarian_conflict():
    response = client.post("/registration/registration", json= {"name":"testinglibrarian", "email":"testing@test.com", "username":"testinglibrarianusername","password":"testingpassword", "usertype":"librarian-admin"})
    assert response.status_code == 200

    response = client.post("/registration/registration", json= {"name":"testinglibrarian", "email":"testing@test.com", "username":"testinglibrarianusername","password":"testingpassword", "usertype":"librarian-admin"})
    assert response.status_code == 409
    assert response.json()["detail"] == "User already exists."