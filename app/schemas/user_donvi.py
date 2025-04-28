from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional
class UserDonvi(BaseModel):
    user_id: UUID4
    unit_id: UUID4
class UserDonviCreate(UserDonvi):
    pass
class UserDonviUpdate(UserDonvi):
    pass

class userunitoutDB(UserDonvi):
    int: int
    updated_at: datetime
    created_at: datetime
