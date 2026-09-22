from fastapi import FastAPI
from model.test import Item
import psycopg2
from decouple import config
from psycopg2.extras import RealDictCursor

app = FastAPI()


while True:
    try:
        cnn = psycopg2.connect(
            host= 'localhost',
            database='practicefastapi',
            user=config('DB_USERNAME'),
            password=config('DB_PASSWORD'),
            cursor_factory=RealDictCursor
        )
        cursor = cnn.cursor()
        print("DB is connected successfully")
        break
    except Exception as e:
        print(e)
        
        


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