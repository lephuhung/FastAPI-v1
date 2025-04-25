from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.social_account_link import SocialAccountLinkCreate, SocialAccountLinkUpdate, SocialAccountLink
from app.crud.crud_social_account_link import social_account_link
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/social-account-links", tags=["Social Account Links"])

@router.get("/", response_model=List[SocialAccountLink])
async def get_social_account_links(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve social account links.
    """
    social_account_links = social_account_link.get_multi(db, skip=skip, limit=limit)
    return social_account_links

@router.post("/", response_model=SocialAccountLink)
async def create_social_account_link(
    *,
    db: Session = Depends(deps.get_db),
    social_account_link_in: SocialAccountLinkCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new social account link.
    """
    social_account_link_obj = social_account_link.create(db=db, obj_in=social_account_link_in)
    return social_account_link_obj

@router.put("/{id}", response_model=SocialAccountLink)
async def update_social_account_link(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    social_account_link_in: SocialAccountLinkUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a social account link.
    """
    social_account_link_obj = social_account_link.get(db=db, id=id)
    if not social_account_link_obj:
        raise HTTPException(status_code=404, detail="Social account link not found")
    social_account_link_obj = social_account_link.update(db=db, db_obj=social_account_link_obj, obj_in=social_account_link_in)
    return social_account_link_obj

@router.get("/{id}", response_model=SocialAccountLink)
async def get_social_account_link(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get social account link by ID.
    """
    social_account_link_obj = social_account_link.get(db=db, id=id)
    if not social_account_link_obj:
        raise HTTPException(status_code=404, detail="Social account link not found")
    return social_account_link_obj

@router.delete("/{id}", response_model=SocialAccountLink)
async def delete_social_account_link(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a social account link.
    """
    social_account_link_obj = social_account_link.get(db=db, id=id)
    if not social_account_link_obj:
        raise HTTPException(status_code=404, detail="Social account link not found")
    social_account_link_obj = social_account_link.remove(db=db, id=id)
    return social_account_link_obj 