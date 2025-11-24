from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

itens_db = [
    {"id": 1, "nome": "Item 1", "descricao": "Descrição do Item 1"},
    {"id": 2, "nome": "Item 2", "descricao": "Descrição do Item 2"},
]

class Item(BaseModel):
    id: int
    nome: str
    descricao: str

@app.get("/items/{item_id}")
def buscar_item(item_id: int):
    for item in itens_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não existe")
