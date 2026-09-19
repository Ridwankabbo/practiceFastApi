from pydantic import BaseModel

class Item(BaseModel):
    
    name:str
    discription: str 
    price: float