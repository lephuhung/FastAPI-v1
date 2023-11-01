from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class model_has_tags(BaseModel):
    id : Optional[int]
    model_id : Optional[int]
    tags_id : Optional[int]

    class Config:
        from_attributes = True

class model_has_tags_date(model_has_tags):
    created_at : datetime
    updated_at : datetime