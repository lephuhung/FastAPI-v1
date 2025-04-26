from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.user_permission import UserPermissionCreate, UserPermissionUpdate, UserPermission
from app.crud.crud_user_permission import user_permission
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user-permissions", tags=["User Permissions"])

@router.get("/", response_model=List[UserPermission])
async def get_user_permissions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Retrieve user permissions.
    """
    user_permissions = user_permission.get_multi(db, skip=skip, limit=limit)
    return user_permissions

@router.post("/", response_model=UserPermission)
async def create_user_permission(
    *,
    db: Session = Depends(deps.get_db),
    user_permission_in: UserPermissionCreate,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Create new user permission.
    """
    user_permission_obj = user_permission.create(db=db, obj_in=user_permission_in)
    return user_permission_obj

@router.put("/{id}", response_model=UserPermission)
async def update_user_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    user_permission_in: UserPermissionUpdate,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update a user permission.
    """
    user_permission_obj = user_permission.get(db=db, id=id)
    if not user_permission_obj:
        raise HTTPException(status_code=404, detail="User permission not found")
    user_permission_obj = user_permission.update(db=db, db_obj=user_permission_obj, obj_in=user_permission_in)
    return user_permission_obj

@router.get("/{id}", response_model=UserPermission)
async def get_user_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get user permission by ID.
    """
    user_permission_obj = user_permission.get(db=db, id=id)
    if not user_permission_obj:
        raise HTTPException(status_code=404, detail="User permission not found")
    return user_permission_obj

@router.delete("/{id}", response_model=UserPermission)
async def delete_user_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Delete a user permission.
    """
    user_permission_obj = user_permission.get(db=db, id=id)
    if not user_permission_obj:
        raise HTTPException(status_code=404, detail="User permission not found")
    user_permission_obj = user_permission.remove(db=db, id=id)
    return user_permission_obj 