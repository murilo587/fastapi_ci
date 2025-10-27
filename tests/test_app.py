from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_alunos_sucesso():
    response = client.get("/alunos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_buscar_aluno_por_id_sucesso():
    response = client.get("/alunos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_buscar_aluno_por_id_falha():
    response = client.get("/alunos/999")
    assert response.status_code == 404


def test_criar_aluno_sucesso():
    novo = {"id": 2, "nome": "Novo Aluno", "email": "novo@exemplo.com"}
    response = client.post("/alunos", json=novo)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Novo Aluno"


def test_criar_aluno_falha_id_duplicado():
    duplicado = {"id": 1, "nome": "Duplicado", "email": "dup@exemplo.com"}
    response = client.post("/alunos", json=duplicado)
    assert response.status_code == 400
