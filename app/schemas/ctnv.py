from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ctnv(BaseModel):
    
    name: Optional[str]

    class Config:
        from_attributes = True
class ctnvcreate(ctnv):
    pass

class ctnvupdate(ctnv):
    id: Optional[int]
    
class ctnv_date(ctnv):
    created_at : datetime
    updated_at : datetime