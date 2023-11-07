from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class color(BaseModel):
    id: Optional[int]
    color: Optional[str]

    class Config:
        from_attributes = True

class color_date(color):
    created_at : datetime
    updated_at : datetime