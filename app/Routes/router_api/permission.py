from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.permission import PermissionCreate, PermissionUpdate, Permission
from app.crud.crud_permission import permission
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/permissions", tags=["Permissions"])

@router.get("/", response_model=List[Permission])
async def get_permissions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Retrieve permissions.
    """
    permissions = permission.get_multi(db, skip=skip, limit=limit)
    return permissions

@router.post("/", response_model=Permission)
async def create_permission(
    *,
    db: Session = Depends(deps.get_db),
    permission_in: PermissionCreate,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Create new permission.
    """
    permission_obj = permission.create(db=db, obj_in=permission_in)
    return permission_obj

@router.put("/{id}", response_model=Permission)
async def update_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    permission_in: PermissionUpdate,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update a permission.
    """
    permission_obj = permission.get(db=db, id=id)
    if not permission_obj:
        raise HTTPException(status_code=404, detail="Permission not found")
    permission_obj = permission.update(db=db, db_obj=permission_obj, obj_in=permission_in)
    return permission_obj

@router.get("/{id}", response_model=Permission)
async def get_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get permission by ID.
    """
    permission_obj = permission.get(db=db, id=id)
    if not permission_obj:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission_obj

@router.delete("/{id}", response_model=Permission)
async def delete_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Delete a permission.
    """
    permission_obj = permission.get(db=db, id=id)
    if not permission_obj:
        raise HTTPException(status_code=404, detail="Permission not found")
    permission_obj = permission.remove(db=db, id=id)
    return permission_obj 