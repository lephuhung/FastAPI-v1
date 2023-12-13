from app.crud.base import CRUDBase
from app.models.tags import Tags
from app.schemas.tags import tagscreate, tagsupdate
from sqlalchemy.orm import Session
class CRUDTags(CRUDBase[Tags, tagscreate, tagsupdate]):
    def get_tags_by_id(self, id: int, db: Session):
        return db.query(Tags).filter(Tags.id == id).first()


crud_tags = CRUDTags(Tags)