from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class relationship(BaseModel):
    
    name: Optional[str]

    class Config:
        from_attributes = True
        
class relationshipcreate(relationship):
    pass

class relationshipupdate(relationship):
    id: Optional[int]
    
class relationship_date(relationship):
    created_at : datetime
    updated_at : datetime