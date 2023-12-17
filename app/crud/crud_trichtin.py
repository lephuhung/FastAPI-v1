from app.crud.base import CRUDBase
from app.models.trichtin import trichtin
from app.schemas.trichtin import trichtinCreate, trichtinUpdate

class CRUD_Trichtin(CRUDBase[trichtin, trichtinCreate, trichtinUpdate]):
    pass

crud_trichtin = CRUD_Trichtin(trichtin)