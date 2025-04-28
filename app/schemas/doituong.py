from pydantic import UUID4, BaseModel
from typing import Optional
from datetime import datetime, date


class individual(BaseModel):

    full_name: Optional[str]
    national_id: Optional[str]
    citizen_id: Optional[str]
    date_of_birth: Optional[date]
    # True is Nam, False is Nu
    is_male: bool
    hometown: Optional[str]
    additional_info: Optional[str]
    phone_number: Optional[str]
    is_kol: bool
    image_url: Optional[str]


class individualcreate(individual):
    task_id: Optional[int]
    unit_id: Optional[UUID4]

    def get_individual_instance(self) -> individual:
        return individual(
            full_name= self.full_name,
            national_id = self.national_id,
            citizen_id = self.citizen_id,
            date_of_birth= self.date_of_birth,
            # True is Nam, False is Nu
            is_male=self.is_male,
            hometown = self.hometown,
            additional_info= self.additional_info,
            phone_number= self.phone_number,
            is_kol = self.is_kol,
            image_url= self.image_url
        )


class individualupdate(individualcreate):
    id: UUID4
    pass


class individualoutDB(individual):
    created_at: datetime
    updated_at: datetime
