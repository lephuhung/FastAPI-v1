from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.individual import Individual
from app.schemas.individual import IndividualCreate, IndividualUpdate
from pydantic import UUID4
from datetime import date


class CRUDIndividual(CRUDBase[Individual, IndividualCreate, IndividualUpdate]):
    def get_by_phone_number(self, db: Session, *, phone_number: str) -> Optional[Individual]:
        return db.query(Individual).filter(Individual.phone_number == phone_number).first()

    def get_by_national_id(self, db: Session, *, national_id: str) -> Optional[Individual]:
        return db.query(Individual).filter(Individual.national_id == national_id).first()

    def get_by_citizen_id(self, db: Session, *, citizen_id: str) -> Optional[Individual]:
        return db.query(Individual).filter(Individual.citizen_id == citizen_id).first()

    def get_by_name(self, db: Session, *, name: str) -> List[Individual]:
        return db.query(Individual).filter(Individual.full_name.ilike(f"%{name}%")).all()

    def get_kols(self, db: Session) -> List[Individual]:
        return db.query(Individual).filter(Individual.is_kol == True).all()

    def get_by_date_of_birth(self, db: Session, *, dob: date) -> List[Individual]:
        return db.query(Individual).filter(Individual.date_of_birth == dob).all()

    def get_by_gender(self, db: Session, *, is_male: bool) -> List[Individual]:
        return db.query(Individual).filter(Individual.is_male == is_male).all()

    def get_by_hometown(self, db: Session, *, hometown: str) -> List[Individual]:
        return db.query(Individual).filter(Individual.hometown.ilike(f"%{hometown}%")).all()


individual = CRUDIndividual(Individual) 