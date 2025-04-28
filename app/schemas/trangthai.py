from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class status(BaseModel):
    
    name: Optional[str]
    color: Optional[str]
    class Config:
        from_attributes = True
        
class trangthaicreate(status):
    pass

class trangthaiupdate(status):
    id: Optional[int]
    
class trangthai_date(status):
    created_at : datetime
    updated_at : datetime