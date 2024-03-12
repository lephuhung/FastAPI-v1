from app.crud.base import CRUDBase
from app.models.trichtin import trichtin
from app.models.user import User
from app.schemas.trichtin import trichtinCreate, trichtinUpdate
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
class CRUD_Trichtin(CRUDBase[trichtin, trichtinCreate, trichtinUpdate]):
    def get_all_by_uid(self,uid: str, db: Session):
        result = (db.query(trichtin.uid.label('uid'), trichtin.ghichu_noidung.label('ghichu_noidung'), trichtin.updated_at.label('updated_at'), 
                    trichtin.uid_vaiao.label('uid_vaiao'), trichtin.nhanxet.label('nhanxet'), trichtin.xuly.label('xuly'), trichtin. created_at.label('created_at'), trichtin.created_at.label('created_at'),
                    User.username.label('username')
                    ).filter(trichtin.uid ==uid)
                    .join(User, User.id == trichtin.user_id)

                    .all()
                    )
        formatted_result = [
        {
            'uid': row.uid,
            'ghichu_noidung': row.ghichu_noidung,
            'updated_at': str(row.updated_at),
            'created_at': str(row.created_at),
            "uid_vaiao": row.uid_vaiao,
            "nhanxet": row.nhanxet,
            'xuly': row.xuly,
            'user': row.username
        }
        for row in result
        ]
        formatted_result_as_dict = [dict(item) for item in formatted_result]
        return JSONResponse(content=formatted_result_as_dict)

    def get_trichtin_by_id(self,id: int, db: Session):
        return db.query(trichtin).filter(trichtin.id == id).first()

crud_trichtin = CRUD_Trichtin(trichtin)