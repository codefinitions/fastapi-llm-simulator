from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_explain_valid():
    payload = {
        "concept": "Machine Learning",
        "audience": "5-year-old"
    }
    response = client.post("/explain", json=payload)
    assert response.status_code == 200
    assert "Machine Learning" in response.json()["concept"]


def test_explain_invalid():
    payload = {
        "concept": "",
        "audience": ""
    }
    response = client.post("/explain", json=payload)
    assert response.status_code == 422  # validation error
