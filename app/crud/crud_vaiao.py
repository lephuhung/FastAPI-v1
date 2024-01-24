from app.crud.base import CRUDBase
from app.models.vaiao import vaiao
from app.models.uid import uid
from app.schemas.vaiao import vaiaocreate, vaiaoupdate
from sqlalchemy.orm import Session, aliased
from fastapi.responses import JSONResponse

class CRUD_Vaiao(CRUDBase[vaiao, vaiaocreate, vaiaoupdate]) :
    def get_all(self, db: Session):
        a1_alias = aliased(uid, name='a1_alias')
        a2_alias = aliased(uid, name='a2_alias')
        B = aliased(vaiao, name='B')
        
# Perform the join query
        result = (
            db.query(B.uid_hoinhom.label('uid_hoinhom'), B.uid_vaiao.label('uid_vaiao'), a1_alias.name.label('vaiao_name'), a2_alias.name.label('hoinhom_name'), B.updated_at.label('updated_at'), B.active.label('active'))
            .join(B, a1_alias.uid == B.uid_vaiao)
            .join(a2_alias, a2_alias.uid == B.uid_hoinhom)
            .distinct(B.uid_hoinhom, B.uid_vaiao)
            .all()
        )
        formatted_result = [
        {
            'uid_hoinhom': row.uid_hoinhom,
            'uid_vaiao': row.uid_vaiao,
            'vaiao_name': row.vaiao_name,
            'hoinhom_name': row.hoinhom_name,
            'updated_at': str(row.updated_at),
            "active": row.active
        }
        for row in result
        ]
        return JSONResponse(content=formatted_result)

crud_vaiao = CRUD_Vaiao(vaiao)