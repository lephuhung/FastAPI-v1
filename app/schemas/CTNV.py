from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ctnv(BaseModel):
    id: Optional[int]
    ctnv_name: Optional[str]

    class Config:
        from_attributes = True

class ctnv_date(ctnv):
    created_at : datetime
    updated_at : datetime