from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class doituong_uid(BaseModel):
    id: Optional[int]
    doituong_id: Optional[int]
    uid: Optional[str]
    moiquanhe_id: Optional[int]
    color: Optional[str]
    class Config:
        from_attributes = True

class doituong_uid_date(doituong_uid):
    created_at : datetime
    updated_at : datetime