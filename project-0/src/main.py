
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/items/{item_id}")
def read_item (item_id: int):
    if item_id > 50:
        q = "secret boss"
    else:
        q = "Guess a higher value"
    return {"item_id": item_id, "query": q}