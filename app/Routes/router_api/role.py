from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.role import RoleCreate, RoleUpdate, Role
from app.crud.crud_role import role
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=List[Role])
async def get_roles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve roles.
    """
    roles = role.get_multi(db, skip=skip, limit=limit)
    return roles

@router.post("/", response_model=Role)
async def create_role(
    *,
    db: Session = Depends(deps.get_db),
    role_in: RoleCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new role.
    """
    role_obj = role.create(db=db, obj_in=role_in)
    return role_obj

@router.put("/{id}", response_model=Role)
async def update_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    role_in: RoleUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a role.
    """
    role_obj = role.get(db=db, id=id)
    if not role_obj:
        raise HTTPException(status_code=404, detail="Role not found")
    role_obj = role.update(db=db, db_obj=role_obj, obj_in=role_in)
    return role_obj

@router.get("/{id}", response_model=Role)
async def get_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get role by ID.
    """
    role_obj = role.get(db=db, id=id)
    if not role_obj:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_obj

@router.delete("/{id}", response_model=Role)
async def delete_role(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a role.
    """
    role_obj = role.get(db=db, id=id)
    if not role_obj:
        raise HTTPException(status_code=404, detail="Role not found")
    role_obj = role.remove(db=db, id=id)
    return role_obj 