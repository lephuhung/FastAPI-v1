from app.crud.base import CRUDBase
from app.models.quantrivien import quantrivien
from app.schemas.quantrivien import quantriviencreate, quantrivienupdate
from sqlalchemy.orm import Session

class CRUD_Quantrivien(CRUDBase[quantrivien, quantriviencreate, quantrivienupdate]):
    pass

crud_quantrivien = CRUD_Quantrivien(quantrivien)