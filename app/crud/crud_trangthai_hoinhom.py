from app.crud.base import CRUDBase
from app.models.trangthai_hoinhom import trangthai_hoinhom
from app.schemas.trangthai_hoinhom import trangthai_hoinhomcreate, trangthai_hoinhomupdate

class CRUD_TrangthaiHoinhom(CRUDBase[trangthai_hoinhom, trangthai_hoinhomcreate, trangthai_hoinhomupdate]):
    pass

crud_trangthai_hoinhom = CRUD_TrangthaiHoinhom(trangthai_hoinhom)