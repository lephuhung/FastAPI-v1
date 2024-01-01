from app.crud.base import CRUDBase
from app.models.trangthai_hoinhom import trangthai_hoinhom
from app.models.trangthai import trangthai
from app.models.uid import uid
from app.schemas.trangthai_hoinhom import trangthai_hoinhomcreate, trangthai_hoinhomupdate
from sqlalchemy.orm import Session
import json

class CRUD_TrangthaiHoinhom(CRUDBase[trangthai_hoinhom, trangthai_hoinhomcreate, trangthai_hoinhomupdate]):
    def get_all_trangthai_hoinhom(self, uid_id: str ,db: Session):
        data = (db.query(uid.name.label('name'), trangthai.name.label('trangthai'))
                .join(trangthai_hoinhom, trangthai_hoinhom.trangthai_id == trangthai.id)
                .join(uid, uid.uid == trangthai_hoinhom.uid)
                .filter(trangthai_hoinhom.uid ==uid_id)
                ) 
        data_output = {
            "name": data[0].name,  # Assuming there's only one result, adjust as needed
            "trangthai": [item.trangthai for item in data]
            }

        # Convert the data dictionary to a JSON-formatted string
        return data_output

crud_trangthai_hoinhom = CRUD_TrangthaiHoinhom(trangthai_hoinhom)