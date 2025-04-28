from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class individual_unit(BaseModel):
    individual_id: UUID4
    unit_id: UUID4
    CTNV_ID: int

    class Config:
        from_attributes = True
class individual_unitcreate(individual_unit):
    pass

class individual_unitupdate(individual_unit):
    id: Optional[int]

