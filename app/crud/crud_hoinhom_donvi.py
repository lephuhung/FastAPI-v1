from app.crud.base import CRUDBase
from app.models.donvi_hoinhom import donvi_hoinhom
from app.schemas.donvi_hoinhom import hoinhom_donvicreate, hoinhom_donviupdate

class CRUDHoinhom_donvi(CRUDBase[donvi_hoinhom, hoinhom_donvicreate, hoinhom_donviupdate]):
    pass

crud_donvihoinhom = CRUDHoinhom_donvi(donvi_hoinhom)