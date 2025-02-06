from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register():
    response = client.post(
        "/register/", json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert "id" in response.json()


def test_debug_code():
    response = client.post("/debug/", json={"code": "print('Hello')"})
    assert response.status_code == 200
    assert "suggestions" in response.json()
