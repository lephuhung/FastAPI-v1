from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.report import Report
from app.schemas.report import ReportCreate, ReportUpdate
from pydantic import UUID4


class CRUDReport(CRUDBase[Report, ReportCreate, ReportUpdate]):
    def get_by_social_account_uid(
        self, db: Session, *, social_account_uid: str
    ) -> List[Report]:
        return db.query(Report).filter(Report.social_account_uid == social_account_uid).all()

    def get_by_user_id(self, db: Session, *, user_id: UUID4) -> List[Report]:
        return db.query(Report).filter(Report.user_id == user_id).all()

    def get_by_linked_social_account_uid(
        self, db: Session, *, linked_social_account_uid: str
    ) -> List[Report]:
        return db.query(Report).filter(Report.linked_social_account_uid == linked_social_account_uid).all()


report = CRUDReport(Report) 