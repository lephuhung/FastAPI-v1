from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class trangthai_hoinhom(BaseModel):
    
    status: Optional[int]
    uid: Optional[str]
    
    class Config:
        from_attributes = True
        
class trangthai_hoinhomcreate(trangthai_hoinhom):
    pass

class trangthai_hoinhomupdate(trangthai_hoinhom):
    pass
    