from pydantic import  BaseModel
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from datetime import datetime
from typing import Optional

class uid(BaseModel):
    id : Optional[int]
    uid : Optional[str]
    name : Optional[str]
    reaction : Optional[int]
    SDT: Optional[str]
    trangthai_id : Optional[int]
    type_id : Optional [int]
    ghichu : Optional[str]
    Vaiao: bool
    created_at: datetime
    updated_at: datetime