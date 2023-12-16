from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import UUID4
class model_has_tags(BaseModel):
    model_id : Optional[str]
    tags_id : Optional[int]

    class Config:
        from_attributes = True
class model_has_tagscreate(model_has_tags):
    pass

class model_has_tagsupdate(model_has_tags):
    id : Optional[int]

class model_has_tags_date(model_has_tags):
    created_at : datetime
    updated_at : datetime