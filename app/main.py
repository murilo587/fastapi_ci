from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel, EmailStr

app = FastAPI(title="API de Usuários Externa")

class Usuario(BaseModel):
    id: int
    name: str
    email: EmailStr


API_URL = "https://jsonplaceholder.typicode.com/users"


@app.get("/usuarios")
def listar_usuarios():
    response = httpx.get(API_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Erro ao acessar API externa")
    return response.json()


@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    response = httpx.get(f"{API_URL}/{usuario_id}")
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    elif response.status_code != 200:
        raise HTTPException(status_code=502, detail="Erro na API externa")
    return response.json()


@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario):
    response = httpx.post(API_URL, json=usuario.model_dump())
    if response.status_code not in (200, 201):
        raise HTTPException(status_code=502, detail="Erro ao criar usuário externo")
    return response.json()
