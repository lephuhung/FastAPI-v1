from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CharacteristicBase(BaseModel):
    name: str
    color: Optional[str] = None


class CharacteristicCreate(CharacteristicBase):
    pass


class CharacteristicUpdate(CharacteristicBase):
    pass


class CharacteristicInDBBase(CharacteristicBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Characteristic(CharacteristicInDBBase):
    pass


class CharacteristicInDB(CharacteristicInDBBase):
    pass 