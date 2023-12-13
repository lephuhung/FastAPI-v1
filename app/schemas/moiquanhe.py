from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class moiquanhe(BaseModel):
    
    name: Optional[str]

    class Config:
        from_attributes = True
        
class moiquanhecreate(moiquanhe):
    pass

class moiquanheupdate(moiquanhe):
    id: Optional[int]
    
class moiquanhe_date(moiquanhe):
    created_at : datetime
    updated_at : datetime