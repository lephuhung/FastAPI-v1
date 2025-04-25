from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class GroupCharacteristicBase(BaseModel):
    characteristic_id: int
    social_account_uid: str


class GroupCharacteristicCreate(GroupCharacteristicBase):
    pass


class GroupCharacteristicUpdate(GroupCharacteristicBase):
    pass


class GroupCharacteristicInDBBase(GroupCharacteristicBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class GroupCharacteristic(GroupCharacteristicInDBBase):
    pass


class GroupCharacteristicInDB(GroupCharacteristicInDBBase):
    pass 