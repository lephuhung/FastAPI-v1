from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.tag import TagCreate, TagUpdate, Tag
from app.crud.crud_tag import tag
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tags", tags=["Tags"])

@router.get("/", response_model=List[Tag])
async def get_tags(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve tags.
    """
    tags = tag.get_multi(db, skip=skip, limit=limit)
    return tags

@router.post("/", response_model=Tag)
async def create_tag(
    *,
    db: Session = Depends(deps.get_db),
    tag_in: TagCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new tag.
    """
    tag_obj = tag.create(db=db, obj_in=tag_in)
    return tag_obj

@router.put("/{id}", response_model=Tag)
async def update_tag(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    tag_in: TagUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a tag.
    """
    tag_obj = tag.get(db=db, id=id)
    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag not found")
    tag_obj = tag.update(db=db, db_obj=tag_obj, obj_in=tag_in)
    return tag_obj

@router.get("/{id}", response_model=Tag)
async def get_tag(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get tag by ID.
    """
    tag_obj = tag.get(db=db, id=id)
    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag_obj

@router.delete("/{id}", response_model=Tag)
async def delete_tag(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a tag.
    """
    tag_obj = tag.get(db=db, id=id)
    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag not found")
    tag_obj = tag.remove(db=db, id=id)
    return tag_obj 