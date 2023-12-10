from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class tags (BaseModel):

    name: Optional[str]
    color: Optional[str]
    class Config:
        from_attributes = True

class tagscreate (tags):
    pass

class tagsupdate (tags):
    id: Optional[int]


class tags_without_date(tags):
    created_at : datetime
    updated_at : datetime