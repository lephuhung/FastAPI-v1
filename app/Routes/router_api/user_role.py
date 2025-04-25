from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.user_role import UserRoleCreate, UserRoleUpdate, UserRole
from app.crud.crud_user_role import user_role
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user-roles", tags=["User Roles"])

@router.get("/", response_model=List[UserRole])
async def get_user_roles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve user roles.
    """
    user_roles = user_role.get_multi(db, skip=skip, limit=limit)
    return user_roles

@router.post("/", response_model=UserRole)
async def create_user_role(
    *,
    db: Session = Depends(deps.get_db),
    user_role_in: UserRoleCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new user role.
    """
    user_role_obj = user_role.create(db=db, obj_in=user_role_in)
    return user_role_obj

@router.put("/{id}", response_model=UserRole)
async def update_user_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    user_role_in: UserRoleUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a user role.
    """
    user_role_obj = user_role.get(db=db, id=id)
    if not user_role_obj:
        raise HTTPException(status_code=404, detail="User role not found")
    user_role_obj = user_role.update(db=db, db_obj=user_role_obj, obj_in=user_role_in)
    return user_role_obj

@router.get("/{id}", response_model=UserRole)
async def get_user_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get user role by ID.
    """
    user_role_obj = user_role.get(db=db, id=id)
    if not user_role_obj:
        raise HTTPException(status_code=404, detail="User role not found")
    return user_role_obj

@router.delete("/{id}", response_model=UserRole)
async def delete_user_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a user role.
    """
    user_role_obj = user_role.get(db=db, id=id)
    if not user_role_obj:
        raise HTTPException(status_code=404, detail="User role not found")
    user_role_obj = user_role.remove(db=db, id=id)
    return user_role_obj 