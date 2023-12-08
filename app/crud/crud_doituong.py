from  app.crud.base import CRUDBase
from app.models.doituong import Doituong
from app.schemas.doituong import doituongcreate, doituongupdate
class CRUD_DOITUONG (CRUDBase[Doituong, doituongcreate, doituongupdate]):
    pass

crud_doituong = CRUD_DOITUONG(Doituong)