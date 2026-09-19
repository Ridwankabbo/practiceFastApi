from fastapi import FastAPI
from model.test import Item
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}

@app.get('/items')
async def read_items(size:int, limit:int=10):
    return {
        "size": size,
        "limit":limit,
    }
    
@app.get('/items/{items_id}')
async def read_items(item_id:int, q:int | None=None):
    if q:
        return {"item_id":item_id, "q":q}
    
    return {"item_id": item_id}


@app.post("/items/")
async def add_items(item: Item):
    
    return {
        "item":item,
    }