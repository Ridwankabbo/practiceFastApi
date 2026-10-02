from pydantic import BaseModel, ConfigDict


class HeroRead(BaseModel):
    
    id: int
    name: str
    secret_name:str
    age:int
    
    model_config=ConfigDict(from_attributes=True)
    
class TeamRead(BaseModel):
    
    id:int
    name:str
    headquaters:str
    
    model_config = ConfigDict(from_attributes=True)
    
    
    
    