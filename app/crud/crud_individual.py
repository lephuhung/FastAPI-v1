from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.individual import Individual
from app.schemas.individual import IndividualCreate, IndividualUpdate
from pydantic import UUID4


class CRUDIndividual(CRUDBase[Individual, IndividualCreate, IndividualUpdate]):
    def get_by_phone_number(self, db: Session, *, phone_number: str) -> Optional[Individual]:
        return db.query(Individual).filter(Individual.phone_number == phone_number).first()

    def get_by_id_number(self, db: Session, *, id_number: str) -> Optional[Individual]:
        return db.query(Individual).filter(Individual.id_number == id_number).first()

    def get_by_name(self, db: Session, *, name: str) -> List[Individual]:
        return db.query(Individual).filter(Individual.full_name.ilike(f"%{name}%")).all()

    def get_kols(self, db: Session) -> List[Individual]:
        return db.query(Individual).filter(Individual.is_kol == True).all()


individual = CRUDIndividual(Individual) 