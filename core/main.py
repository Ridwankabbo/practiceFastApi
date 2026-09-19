from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from .model import Item
app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
fake_items_db = [
    {"id": 1,"Name":"Mango"},
    {"id": 2,"Name":"Banana"},
    {"id": 3,"Name":"Pinaple"}
]

Items = [
    Item(name="abcd", description = "kdsadfsadjfak",price = 10.0, tax = 5.8),
    Item(name="efgh", description="fsdfsdfgsfk", price=15.0, tax= 6.3),
    Item(name="ijkl", description="dsfgsdfgsdfgasak", price=10.0, tax = 5.8)
]

@app.get('/')
async def hellow_world():
    return {"message":"Hellwo world"}

@app.get('/peramiter/{user_name}')
async def hello_user(user_name:int):
    return {"message":user_name}

@app.get('/model/{model_name}')
async def getModel(model_name:ModelName):
    
    
    if model_name == ModelName.alexnet:
        return {"model name": model_name,"message": "Deep Learning FTW!"}
    elif model_name == ModelName.lenet:
        return {"model name":model_name, "message":"LeCNN all the images"}
    
    return {"message":"Invalid model"}


@app.get("/items/")
async def getItems(skip:int = 0, lemit:int=3):
    return Items

@app.post('/item/')
async def creat_itme(item:Item):
    Items.append(item)
    return item

@app.get('/items/{id}')
async def getItemById(id:int):
    if id < len(Items):
        return Items[id]
    return {"response":"Index out of bounce"}

@app.delete('/items/delete/{id}')
async def deleteItemById(id:int):
    Items.pop(id)
    return {"response":"item removed successfully"}
