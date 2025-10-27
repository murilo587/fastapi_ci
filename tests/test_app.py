import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@pytest.fixture
def mock_usuario():
    return {"id": 1, "name": "Usuário Teste", "email": "teste@exemplo.com"}


@patch("app.main.httpx.get")
def test_listar_usuarios_sucesso(mock_get, mock_usuario):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [mock_usuario]

    response = client.get("/usuarios")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["name"] == "Usuário Teste"


@patch("app.main.httpx.get")
def test_buscar_usuario_sucesso(mock_get, mock_usuario):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_usuario

    response = client.get("/usuarios/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


@patch("app.main.httpx.post")
def test_criar_usuario_sucesso(mock_post, mock_usuario):
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = mock_usuario

    response = client.post("/usuarios", json=mock_usuario)
    assert response.status_code == 201
    assert response.json()["email"] == "teste@exemplo.com"


@patch("app.main.httpx.get")
def test_buscar_usuario_falha_404(mock_get):
    mock_get.return_value.status_code = 404
    response = client.get("/usuarios/999")
    assert response.status_code == 404


@patch("app.main.httpx.post")
def test_criar_usuario_falha_api(mock_post, mock_usuario):
    mock_post.return_value.status_code = 500
    response = client.post("/usuarios", json=mock_usuario)
    assert response.status_code == 502
