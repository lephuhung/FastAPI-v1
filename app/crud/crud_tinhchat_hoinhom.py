from app.crud.base import CRUDBase
from app.models.tinhchat_hoinhom import tinhchat_hoinhom
from app.schemas.tinhchat_hoinhom import tinhchat_hoinhomcreate, tinhchat_hoinhomupdate

class CRUD_Tinhchathoinhom(CRUDBase[tinhchat_hoinhom, tinhchat_hoinhomcreate, tinhchat_hoinhomupdate]):
    pass

crud_tinhchat_hoinhom = CRUD_Tinhchathoinhom(tinhchat_hoinhom)