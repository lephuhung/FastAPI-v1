from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.individual_tag import IndividualTag
from app.schemas.individual_tag import IndividualTagCreate, IndividualTagUpdate
from pydantic import UUID4


class CRUDIndividualTag(CRUDBase[IndividualTag, IndividualTagCreate, IndividualTagUpdate]):
    def get_by_individual_id(self, db: Session, *, individual_id: UUID4) -> List[IndividualTag]:
        return db.query(IndividualTag).filter(IndividualTag.individual_id == individual_id).all()

    def get_by_tag_id(self, db: Session, *, tag_id: int) -> List[IndividualTag]:
        return db.query(IndividualTag).filter(IndividualTag.tag_id == tag_id).all()

    def get_by_individual_and_tag(
        self, db: Session, *, individual_id: UUID4, tag_id: int
    ) -> Optional[IndividualTag]:
        return (
            db.query(IndividualTag)
            .filter(IndividualTag.individual_id == individual_id, IndividualTag.tag_id == tag_id)
            .first()
        )


individual_tag = CRUDIndividualTag(IndividualTag) 