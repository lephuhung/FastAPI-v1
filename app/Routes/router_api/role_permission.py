from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.role_permission import RolePermissionCreate, RolePermissionUpdate, RolePermission
from app.crud.crud_role_permission import role_permission
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/role-permissions", tags=["Role Permissions"])

@router.get("/", response_model=List[RolePermission])
async def get_role_permissions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Retrieve role permissions.
    """
    role_permissions = role_permission.get_multi(db, skip=skip, limit=limit)
    return role_permissions

@router.post("/", response_model=RolePermission)
async def create_role_permission(
    *,
    db: Session = Depends(deps.get_db),
    role_permission_in: RolePermissionCreate,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Create new role permission.
    """
    role_permission_obj = role_permission.create(db=db, obj_in=role_permission_in)
    return role_permission_obj

@router.put("/{id}", response_model=RolePermission)
async def update_role_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    role_permission_in: RolePermissionUpdate,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update a role permission.
    """
    role_permission_obj = role_permission.get(db=db, id=id)
    if not role_permission_obj:
        raise HTTPException(status_code=404, detail="Role permission not found")
    role_permission_obj = role_permission.update(db=db, db_obj=role_permission_obj, obj_in=role_permission_in)
    return role_permission_obj

@router.get("/{id}", response_model=RolePermission)
async def get_role_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get role permission by ID.
    """
    role_permission_obj = role_permission.get(db=db, id=id)
    if not role_permission_obj:
        raise HTTPException(status_code=404, detail="Role permission not found")
    return role_permission_obj

@router.delete("/{id}", response_model=RolePermission)
async def delete_role_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Delete a role permission.
    """
    role_permission_obj = role_permission.get(db=db, id=id)
    if not role_permission_obj:
        raise HTTPException(status_code=404, detail="Role permission not found")
    role_permission_obj = role_permission.remove(db=db, id=id)
    return role_permission_obj 