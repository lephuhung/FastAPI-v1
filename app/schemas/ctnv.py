from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class task(BaseModel):
    
    name: Optional[str]

    class Config:
        from_attributes = True
class taskcreate(task):
    pass

class taskupdate(task):
    id: Optional[int]
    
class task_date(task):
    created_at : datetime
    updated_at : datetime