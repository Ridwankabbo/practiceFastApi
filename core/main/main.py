from fastapi import FastAPI
from model.test import Hero
import psycopg2
from decouple import config
from psycopg2.extras import RealDictCursor

app = FastAPI()


# while True:
#     try:
#         cnn = psycopg2.connect(
#             host= 'localhost',
#             database='practicefastapi',
#             user=config('DB_USERNAME'),
#             password=config('DB_PASSWORD'),
#             cursor_factory=RealDictCursor
#         )
#         cursor = cnn.cursor()
#         print("DB is connected successfully")
#         break
#     except Exception as e:
#         print(e)
        
        


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

from model.test import (
    select_heros,
    select_hero,
    create_hero,
    Hero,
    Team,
    create_team,
    get_teams,
    get_team_by_id
)
@app.get('/items/db/')
async def show_data():
    data = select_heros()
    return data

@app.get("/items/db/get/")
async def show_item(id: int):
    try:
        data = select_hero(id)
        return data
    except Exception as e:
        return f"an error occured {e}"
    
    
@app.post('/items/add/')
async def add_item(item:Hero):
    create_hero(item)
    
    return "added successfully"


@app.get('/team/litst')
async def get_team_list():
    list = get_teams()
    return list

@app.post('/items/team/add')
async def add_team(team:Team):
    create_team(team)
    
    return "Team created successfully"   
from .model_schema import TeamRead
@app.get('/teams/get/{id}', response_model=TeamRead)
async def get_team(id:int):
    item = get_team_by_id(id)
    
    return item
     
     
