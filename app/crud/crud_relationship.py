from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.relationship import Relationship
from app.schemas.relationship import RelationshipCreate, RelationshipUpdate


class CRUDRelationship(CRUDBase[Relationship, RelationshipCreate, RelationshipUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Relationship]:
        return db.query(Relationship).filter(Relationship.name == name).first()


relationship = CRUDRelationship(Relationship) 