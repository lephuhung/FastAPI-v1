from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class trangthai(BaseModel):
    
    name: Optional[str]
    color: Optional[str]
    class Config:
        from_attributes = True
        
class trangthaicreate(trangthai):
    pass

class trangthaiupdate(trangthai):
    id: Optional[int]
    
class trangthai_date(trangthai):
    created_at : datetime
    updated_at : datetime