from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class type(BaseModel):
    
    name: Optional[str]
    class Config:
        from_attributes = True
        
class typecreate(type):
    pass

class typeupdate(type):
    id: Optional[int]
    
class type_date(type):
    created_at : datetime
    updated_at : datetime