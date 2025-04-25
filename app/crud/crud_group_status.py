from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.group_status import GroupStatus
from app.schemas.group_status import GroupStatusCreate, GroupStatusUpdate


class CRUDGroupStatus(CRUDBase[GroupStatus, GroupStatusCreate, GroupStatusUpdate]):
    def get_by_status_id(self, db: Session, *, status_id: int) -> List[GroupStatus]:
        return db.query(GroupStatus).filter(GroupStatus.status_id == status_id).all()

    def get_by_social_account_uid(
        self, db: Session, *, social_account_uid: str
    ) -> List[GroupStatus]:
        return db.query(GroupStatus).filter(GroupStatus.social_account_uid == social_account_uid).all()

    def get_by_status_and_social_account(
        self, db: Session, *, status_id: int, social_account_uid: str
    ) -> Optional[GroupStatus]:
        return (
            db.query(GroupStatus)
            .filter(
                GroupStatus.status_id == status_id,
                GroupStatus.social_account_uid == social_account_uid
            )
            .first()
        )


group_status = CRUDGroupStatus(GroupStatus) 