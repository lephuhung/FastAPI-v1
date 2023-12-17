from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class tinhchat_hoinhom(BaseModel):
    
    tinhchat_id: Optional[int]
    uid: Optional[str]
    class Config:
        from_attributes = True
        
class tinhchat_hoinhomcreate(tinhchat_hoinhom):
    pass

class tinhchat_hoinhomupdate(tinhchat_hoinhom):
    pass
    