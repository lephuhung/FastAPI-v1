from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class tags (BaseModel):
    id: Optional[int]
    name: Optional[str]
    

    class Config:
        from_attributes = True

class tags_without_date(tags):
    created_at : datetime
    updated_at : datetime