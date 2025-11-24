from fastapi import FastAPI, HTTPException

app = FastAPI()

items_db = {
    1: {"id": 1, "nome": "Item exemplo"}
}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items_db:
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item não existe")
