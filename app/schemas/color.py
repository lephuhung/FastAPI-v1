from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class color(BaseModel):
    
    name: Optional[str]
    color: Optional[str]

    class Config:
        from_attributes = True
class colorcreate(color):
    pass

class colorupdate(color):
    id: Optional[int]
    
class color_date(color):
    created_at : datetime
    updated_at : datetime