from fastapi import APIRouter, Depends, HTTPException, Security, Response
from typing import List
from app.schemas.individual_tag import IndividualTagCreate, IndividualTagUpdate, IndividualTag
from app.crud.crud_individual_tag import individual_tag
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/individual-tags", tags=["Đối tượng Tags"])


@router.get("/", response_model=List[IndividualTag])
async def get_individual_tags(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve individual tags.
    """
    individual_tags = individual_tag.get_multi(db, skip=skip, limit=limit)
    return individual_tags


@router.post("/", response_model=IndividualTag)
async def create_individual_tag(
    *,
    db: Session = Depends(deps.get_db),
    individual_tag_in: IndividualTagCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new individual tag.
    """
    individual_tag_obj = individual_tag.create(db=db, obj_in=individual_tag_in)
    return individual_tag_obj


@router.put("/{id}", response_model=IndividualTag)
async def update_individual_tag(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    individual_tag_in: IndividualTagUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an individual tag.
    """
    individual_tag_obj = individual_tag.get(db=db, id=id)
    if not individual_tag_obj:
        raise HTTPException(status_code=404, detail="Individual tag not found")
    individual_tag_obj = individual_tag.update(db=db, db_obj=individual_tag_obj, obj_in=individual_tag_in)
    return individual_tag_obj


@router.get("/{id}", response_model=IndividualTag)
async def get_individual_tag(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get individual tag by ID.
    """
    individual_tag_obj = individual_tag.get(db=db, id=id)
    if not individual_tag_obj:
        raise HTTPException(status_code=404, detail="Individual tag not found")
    return individual_tag_obj


@router.delete("/{id}", response_model=IndividualTag)
async def delete_individual_tag(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete an individual tag.
    """
    individual_tag_obj = individual_tag.get(db=db, id=id)
    if not individual_tag_obj:
        raise HTTPException(status_code=404, detail="Individual tag not found")
    individual_tag_obj = individual_tag.remove(db=db, id=id)
    return individual_tag_obj


@router.get("/individual/{individual_id}", response_model=List[IndividualTag])
async def get_individual_tags_by_individual(
    *,
    db: Session = Depends(deps.get_db),
    individual_id: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get individual tags by individual ID.
    """
    individual_tags = individual_tag.get_all_by_individual_id(db=db, individual_id=individual_id)
    return individual_tags


@router.get("/tag/{tag_id}", response_model=List[IndividualTag])
async def get_individual_tags_by_tag(
    *,
    db: Session = Depends(deps.get_db),
    tag_id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get individual tags by tag ID.
    """
    individual_tags = individual_tag.get_all_by_tag_id(db=db, tag_id=tag_id)
    return individual_tags 