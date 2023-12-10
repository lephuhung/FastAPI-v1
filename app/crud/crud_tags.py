from app.crud.base import CRUDBase
from app.models.tags import Tags
from app.schemas.tags import tagscreate, tagsupdate

class CRUDTags(CRUDBase[Tags, tagscreate, tagsupdate]):
    pass

crud_tags = CRUDTags(Tags)