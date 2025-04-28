from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class characteristic(BaseModel):
    
    name: Optional[str]
    color: Optional[str]
    class Config:
        from_attributes = True
        
class characteristiccreate(characteristic):
    pass

class characteristicupdate(characteristic):
    id: Optional[int]
    
class characteristic_date(characteristic):
    created_at : datetime
    updated_at : datetime