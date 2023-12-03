from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional
class UserDonvi(BaseModel):
    user_id: UUID4
    donvi_id: UUID4
class UserDonviCreate(UserDonvi):
    pass
class UserDonviUpdate(UserDonvi):
    pass

class userdonvioutDB(UserDonvi):
    int: int
    updated_at: datetime
    created_at: datetime
