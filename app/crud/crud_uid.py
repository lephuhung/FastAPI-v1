from app.crud.base import CRUDBase
from app.models.uid import uid
from app.schemas.uid import uidCreate, uidUpdate
class CRUDUid (CRUDBase[uid,uidCreate, uidUpdate]):
    pass

crud_uid = CRUDUid(uid)