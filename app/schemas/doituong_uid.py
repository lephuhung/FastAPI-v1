from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import UUID4

class doituong_uid(BaseModel):
    doituong_id: Optional[UUID4]
    uid: Optional[str]
    Moiquanhe_id: Optional[int]
    class Config:
        from_attributes = True
class doituong_uidcreate(doituong_uid):
    pass

class doituong_uidupdate(doituong_uid):
    pass

class doituong_uid_date(doituong_uid):
    created_at : datetime
    updated_at : datetime