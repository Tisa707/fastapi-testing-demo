# test_regression.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_addition_logic():
    response = client.get("/add?a=10&b=20")
    assert response.status_code == 200
    assert response.json() == {"result": 30}
