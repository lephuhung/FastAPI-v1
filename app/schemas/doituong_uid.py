from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import UUID4

class individual_uid(BaseModel):
    individual_id: Optional[UUID4]
    uid: Optional[str]
    relationship_id: Optional[int]
    class Config:
        from_attributes = True
class individual_uidcreate(individual_uid):
    pass

class individual_uidupdate(individual_uid):
    pass

class individual_uid_date(individual_uid):
    created_at : datetime
    updated_at : datetime