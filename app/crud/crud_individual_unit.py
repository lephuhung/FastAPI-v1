from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.individual_unit import IndividualUnit
from app.schemas.individual_unit import IndividualUnitCreate, IndividualUnitUpdate
from pydantic import UUID4


class CRUDIndividualUnit(CRUDBase[IndividualUnit, IndividualUnitCreate, IndividualUnitUpdate]):
    def get_by_unit_id(self, db: Session, *, unit_id: UUID4) -> List[IndividualUnit]:
        return db.query(IndividualUnit).filter(IndividualUnit.unit_id == unit_id).all()

    def get_by_individual_id(self, db: Session, *, individual_id: UUID4) -> List[IndividualUnit]:
        return db.query(IndividualUnit).filter(IndividualUnit.individual_id == individual_id).all()

    def get_by_task_id(self, db: Session, *, task_id: int) -> List[IndividualUnit]:
        return db.query(IndividualUnit).filter(IndividualUnit.task_id == task_id).all()

    def get_by_unit_and_individual(
        self, db: Session, *, unit_id: UUID4, individual_id: UUID4
    ) -> Optional[IndividualUnit]:
        return (
            db.query(IndividualUnit)
            .filter(
                IndividualUnit.unit_id == unit_id,
                IndividualUnit.individual_id == individual_id
            )
            .first()
        )


individual_unit = CRUDIndividualUnit(IndividualUnit) 