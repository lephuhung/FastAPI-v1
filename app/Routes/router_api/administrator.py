from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.administrator import AdministratorCreate, AdministratorUpdate, Administrator
from app.crud.crud_administrator import administrator
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/administrators", tags=["Administrators"])

@router.get("/", response_model=List[Administrator])
async def get_administrators(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve administrators.
    """
    administrators = administrator.get_multi(db, skip=skip, limit=limit)
    return administrators

@router.post("/", response_model=Administrator)
async def create_administrator(
    *,
    db: Session = Depends(deps.get_db),
    administrator_in: AdministratorCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new administrator.
    """
    # Check if social account exists
    social_account = db.query("SocialAccount").filter_by(uid=administrator_in.social_account_uid).first()
    if not social_account:
        raise HTTPException(status_code=404, detail="Social account not found")
    
    # Check if relationship exists
    relationship = db.query("Relationship").filter_by(id=administrator_in.relationship_id).first()
    if not relationship:
        raise HTTPException(status_code=404, detail="Relationship not found")
    
    administrator_obj = administrator.create(db=db, obj_in=administrator_in)
    return administrator_obj

@router.put("/{id}", response_model=Administrator)
async def update_administrator(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    administrator_in: AdministratorUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an administrator.
    """
    administrator_obj = administrator.get(db=db, id=id)
    if not administrator_obj:
        raise HTTPException(status_code=404, detail="Administrator not found")
    
    # Check if social account exists if being updated
    if administrator_in.social_account_uid != administrator_obj.social_account_uid:
        social_account = db.query("SocialAccount").filter_by(uid=administrator_in.social_account_uid).first()
        if not social_account:
            raise HTTPException(status_code=404, detail="Social account not found")
    
    # Check if relationship exists if being updated
    if administrator_in.relationship_id != administrator_obj.relationship_id:
        relationship = db.query("Relationship").filter_by(id=administrator_in.relationship_id).first()
        if not relationship:
            raise HTTPException(status_code=404, detail="Relationship not found")
    
    administrator_obj = administrator.update(db=db, db_obj=administrator_obj, obj_in=administrator_in)
    return administrator_obj

@router.get("/{id}", response_model=Administrator)
async def get_administrator(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get administrator by ID.
    """
    administrator_obj = administrator.get(db=db, id=id)
    if not administrator_obj:
        raise HTTPException(status_code=404, detail="Administrator not found")
    return administrator_obj

@router.get("/uid/{uid_administrator}", response_model=Administrator)
async def get_administrator_by_uid(
    *,
    db: Session = Depends(deps.get_db),
    uid_administrator: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get administrator by UID.
    """
    administrator_obj = administrator.get_by_uid_administrator(db=db, uid_administrator=uid_administrator)
    if not administrator_obj:
        raise HTTPException(status_code=404, detail="Administrator not found")
    return administrator_obj

@router.get("/social-account/{social_account_uid}", response_model=List[Administrator])
async def get_administrators_by_social_account(
    *,
    db: Session = Depends(deps.get_db),
    social_account_uid: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get administrators by social account UID.
    """
    administrators = administrator.get_by_social_account_uid(db=db, social_account_uid=social_account_uid)
    return administrators

@router.get("/relationship/{relationship_id}", response_model=List[Administrator])
async def get_administrators_by_relationship(
    *,
    db: Session = Depends(deps.get_db),
    relationship_id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get administrators by relationship ID.
    """
    administrators = administrator.get_by_relationship_id(db=db, relationship_id=relationship_id)
    return administrators

@router.delete("/{id}", response_model=Administrator)
async def delete_administrator(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete an administrator.
    """
    administrator_obj = administrator.get(db=db, id=id)
    if not administrator_obj:
        raise HTTPException(status_code=404, detail="Administrator not found")
    administrator_obj = administrator.remove(db=db, id=id)
    return administrator_obj 