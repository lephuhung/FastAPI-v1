from typing import Optional
from pydantic import BaseModel, UUID4


class Donvi(BaseModel):
    name: str
class DonviCreate(Donvi):
    pass
class DonviUpdate(Donvi):
    id: UUID4