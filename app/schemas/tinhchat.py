from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class tinhchat(BaseModel):
    
    name: Optional[str]
    color: Optional[str]
    class Config:
        from_attributes = True
        
class tinhchatcreate(tinhchat):
    pass

class tinhchatupdate(tinhchat):
    id: Optional[int]
    
class tinhchat_date(tinhchat):
    created_at : datetime
    updated_at : datetime