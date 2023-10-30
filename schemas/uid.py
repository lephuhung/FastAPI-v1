from pydantic import  BaseModel, Integer, String
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
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
    Vaiao: Boolean
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )