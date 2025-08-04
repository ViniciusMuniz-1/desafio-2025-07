from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_wrap():
    response = client.post("/quebrar-texto", json={"text":  "Teste simples", "limit": 10})
    assert response.status_code == 200
    assert response.json()["lines"] == ["This is a", "simple", "test."]

def test_justify():
    response = client.post("/justificar-texto", json={"text": "Teste", "limit": 20})
    lines = response.json()["lines"]
    assert len(lines) > 0
    assert all(len(line) <= 20 for line in lines)
