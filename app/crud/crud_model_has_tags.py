from app.crud.base import CRUDBase
from app.models.model_has_tags import model_has_tags
from app.models.tags import Tags
from app.schemas.model_has_tags import model_has_tagscreate, model_has_tagsupdate
from sqlalchemy.orm import Session
class CRUDModel_has_tags(CRUDBase[model_has_tags, model_has_tagscreate, model_has_tagsupdate]):
    def get_tags_by_model_id(self, model_id: str, db: Session):
       data =(db.query(Tags.color, Tags.name).
       join(model_has_tags, model_has_tags.tags_id== Tags.id)
       .filter(model_has_tags.model_id==model_id)
       .all())
       return data

crud_model_has_tags = CRUDModel_has_tags(model_has_tags)