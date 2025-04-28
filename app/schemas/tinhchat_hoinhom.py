from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class characteristic_hoinhom(BaseModel):
    
    characteristic_id: Optional[int]
    uid: Optional[str]
    class Config:
        from_attributes = True
        
class characteristic_hoinhomcreate(characteristic_hoinhom):
    pass

class characteristic_hoinhomupdate(characteristic_hoinhom):
    pass
    