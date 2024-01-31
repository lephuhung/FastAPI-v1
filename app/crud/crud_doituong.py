from  app.crud.base import CRUDBase
from pydantic import UUID4
from app.models.doituong import Doituong
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.schemas.doituong import doituongcreate, doituongupdate
from fastapi.responses import JSONResponse
class CRUD_DOITUONG (CRUDBase[Doituong, doituongcreate, doituongupdate]):
    def get_doituong_by_id(self, doituong_id: UUID4, db: Session):
        return db.query(Doituong).filter(Doituong.id == doituong_id).first()

    def get_details(self, doituong_id: UUID4, db:Session):
        details_count = db.query(Doituong.id.label('id'), Doituong.client_name.label('name'), func.count(Doituong.id).label('count')).filter(Doituong.id == doituong_id).group_by(Doituong.id)
        formatted_result = [
        {
            'id': str(row.id),
            'name': row.name,
            'count': row.count

        }
        for row in details_count
        ]
        return JSONResponse(content=formatted_result)
crud_doituong = CRUD_DOITUONG(Doituong)