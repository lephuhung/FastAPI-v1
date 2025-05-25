from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.role_permission import RolePermissionCreate, RolePermissionUpdate, RolePermission
from app.crud.crud_role_permission import role_permission
from app.crud.crud_role import role as role_crud
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4, BaseModel

class PermissionResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class RoleInfoResponse(BaseModel):
    id: UUID4
    name: str
    permissions: List[PermissionResponse]

    class Config:
        from_attributes = True

class UpdateRolePermissionsRequest(BaseModel):
    permission_ids: List[int]

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
    id: str,
    # current_user=Security(deps.get_current_superadmin, scopes=[]),
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

@router.get("/by-role/{role_id}", response_model=List[PermissionResponse])
async def get_role_permissions_by_role_id(
    *,
    db: Session = Depends(deps.get_db),
    role_id: UUID4,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get all permissions for a specific role ID.
    Returns an array of permissions with their IDs and names.
    If no permissions are found, returns an empty array.
    """
    role_permissions = role_permission.get_by_role_id(db=db, role_id=role_id)
    
    # Extract permission details from the role_permissions
    permissions = [
        PermissionResponse(
            id=rp.permission.id,
            name=rp.permission.name
        )
        for rp in role_permissions
    ] if role_permissions else []
    
    return permissions 

@router.get("/superadmin", response_model=RoleInfoResponse)
async def get_superadmin_permissions(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get superadmin role info and its permissions.
    """
    role_obj = role_crud.get_by_name(db=db, name="superadmin")
    if not role_obj:
        raise HTTPException(status_code=404, detail="Superadmin role not found")
    
    role_permissions = role_permission.get_by_role_id(db=db, role_id=role_obj.id)
    permissions = [
        PermissionResponse(id=rp.permission.id, name=rp.permission.name)
        for rp in role_permissions
    ] if role_permissions else []
    
    return RoleInfoResponse(
        id=role_obj.id,
        name=role_obj.name,
        permissions=permissions
    )

@router.get("/roles/admin", response_model=RoleInfoResponse)
async def get_admin_role_permissions(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get admin role info and its permissions.
    """
    role_obj = role_crud.get_by_name(db=db, name="admin")
    if not role_obj:
        raise HTTPException(status_code=404, detail="Admin role not found")
    
    role_permissions = role_permission.get_by_role_id(db=db, role_id=role_obj.id)
    permissions = [
        PermissionResponse(id=rp.permission.id, name=rp.permission.name)
        for rp in role_permissions
    ] if role_permissions else []
    
    return RoleInfoResponse(
        id=role_obj.id,
        name=role_obj.name,
        permissions=permissions
    )

@router.get("/roles/cax", response_model=RoleInfoResponse)
async def get_xa_role_permissions(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get xa role info and its permissions.
    """
    role_obj = role_crud.get_by_name(db=db, name="cax")
    if not role_obj:
        raise HTTPException(status_code=404, detail="Xa role not found")
    
    role_permissions = role_permission.get_by_role_id(db=db, role_id=role_obj.id)
    permissions = [
        PermissionResponse(id=rp.permission.id, name=rp.permission.name)
        for rp in role_permissions
    ] if role_permissions else []
    
    return RoleInfoResponse(
        id=role_obj.id,
        name=role_obj.name,
        permissions=permissions
    )

@router.get("/roles/phong", response_model=RoleInfoResponse)
async def get_phong_role_permissions(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get phong role info and its permissions.
    """
    role_obj = role_crud.get_by_name(db=db, name="phong")
    if not role_obj:
        raise HTTPException(status_code=404, detail="Phong role not found")
    
    role_permissions = role_permission.get_by_role_id(db=db, role_id=role_obj.id)
    permissions = [
        PermissionResponse(id=rp.permission.id, name=rp.permission.name)
        for rp in role_permissions
    ] if role_permissions else []
    
    return RoleInfoResponse(
        id=role_obj.id,
        name=role_obj.name,
        permissions=permissions
    )

@router.get("/roles/doi", response_model=RoleInfoResponse)
async def get_doi_role_permissions(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get doi role info and its permissions.
    """
    role_obj = role_crud.get_by_name(db=db, name="doi")
    if not role_obj:
        raise HTTPException(status_code=404, detail="Doi role not found")
    
    role_permissions = role_permission.get_by_role_id(db=db, role_id=role_obj.id)
    permissions = [
        PermissionResponse(id=rp.permission.id, name=rp.permission.name)
        for rp in role_permissions
    ] if role_permissions else []
    
    return RoleInfoResponse(
        id=role_obj.id,
        name=role_obj.name,
        permissions=permissions
    )

@router.put("/roles/{role_name}/permissions", response_model=RoleInfoResponse)
async def update_role_permissions(
    *,
    db: Session = Depends(deps.get_db),
    role_name: str,
    permissions_update: UpdateRolePermissionsRequest,
    current_user=Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update permissions for a specific role.
    """
    # Get the role
    role_obj = role_crud.get_by_name(db=db, name=role_name)
    if not role_obj:
        raise HTTPException(status_code=404, detail=f"Role {role_name} not found")
    
    # Delete existing permissions
    existing_permissions = role_permission.get_by_role_id(db=db, role_id=role_obj.id)
    for perm in existing_permissions:
        db.delete(perm)
    
    # Add new permissions
    new_permissions = []
    for permission_id in permissions_update.permission_ids:
        permission_data = RolePermissionCreate(
            role_id=role_obj.id,
            permission_id=permission_id
        )
        new_perm = role_permission.create(db=db, obj_in=permission_data)
        new_permissions.append(new_perm)
    
    db.commit()
    
    # Return updated permissions
    updated_permissions = role_permission.get_by_role_id(db=db, role_id=role_obj.id)
    permissions = [
        PermissionResponse(id=rp.permission.id, name=rp.permission.name)
        for rp in updated_permissions
    ] if updated_permissions else []
    
    return RoleInfoResponse(
        id=role_obj.id,
        name=role_obj.name,
        permissions=permissions
    ) 