from app.crud.base import CRUDBase
from app.models.vaiao import vaiao
from app.schemas.vaiao import vaiaocreate, vaiaoupdate
from sqlalchemy.orm import Session

class CRUD_Vaiao(CRUDBase[vaiao, vaiaocreate, vaiaoupdate]) :
    pass

crud_vaiao = CRUD_Vaiao(vaiao)