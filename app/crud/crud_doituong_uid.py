from  app.crud.base import CRUDBase
from app.models.doituong_uid import Doituong_UID
from app.schemas.doituong_uid import doituong_uidcreate, doituong_uidupdate


class CRUD_DoituongUID(CRUDBase[Doituong_UID, doituong_uidcreate, doituong_uidupdate]):
    pass

crud_doituong_uid= CRUD_DoituongUID(Doituong_UID)