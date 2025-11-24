from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_buscar_item_existente():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "nome": "Item exemplo"}

def test_buscar_item_inexistente():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não existe"}
