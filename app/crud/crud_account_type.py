from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.account_type import AccountType
from app.schemas.account_type import AccountTypeCreate, AccountTypeUpdate


class CRUDAccountType(CRUDBase[AccountType, AccountTypeCreate, AccountTypeUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[AccountType]:
        return db.query(AccountType).filter(AccountType.name == name).first()


account_type = CRUDAccountType(AccountType) 