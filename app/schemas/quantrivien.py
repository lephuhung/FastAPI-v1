from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class quantrivien(BaseModel):
    uid: Optional[str]
    uid_facebook: Optional[str]
    moiquanhe_id: Optional[int]

    class Config:
        from_attributes = True
class quantriviencreate(quantrivien):
    pass

class quantrivienupdate(quantrivien):
    pass

class quantrivien_date(quantrivien):
    created_at : datetime
    updated_at : datetime