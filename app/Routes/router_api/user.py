from fastapi import APIRouter, Body, Depends, HTTPException, Security, Depends
from typing import Annotated, List, Optional
from app.Routes import deps
from sqlalchemy.orm import Session
from app.core.config import settings
from app import schemas, models
from app.crud import crud_user, crud_unit, crud_user_role, crud_user_permission
from datetime import datetime
from app.core.security import get_salt, get_password_hash
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from app.schemas.user import UserCreate, UserUpdate, User, UserMe
from pydantic import BaseModel
import uuid
from uuid import UUID

class UserCreateForm(BaseModel):
    username: str
    password: str
    unit_id: str

class UnitInfo(BaseModel):
    id: UUID
    name: str

class RoleInfo(BaseModel):
    id: UUID
    name: str

class UserResponse(BaseModel):
    id: UUID
    username: str
    is_active: bool
    roles: List[RoleInfo] = []
    unit_id: Optional[UUID] = None
    unit: Optional[UnitInfo] = None

    class Config:
        from_attributes = True

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def get_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user = Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get all users with their roles and unit information.
    """
    users = crud_user.get_multi(db, skip=skip, limit=limit)
    result = []
    
    for user in users:
        # Get roles for the user
        roles = db.query(models.user_role.UserRole).filter(
            models.user_role.UserRole.user_id == user.id
        ).all()
        
        # Get unit information through UserUnit relationship
        user_unit = db.query(models.user_unit.UserUnit).filter(
            models.user_unit.UserUnit.user_id == user.id
        ).first()
        
        unit = None
        unit_id = None
        if user_unit:
            unit = db.query(models.unit.Unit).filter(
                models.unit.Unit.id == user_unit.unit_id
            ).first()
            unit_id = user_unit.unit_id
        
        # Create role info objects
        role_info_list = []
        for role in roles:
            role_obj = db.query(models.role.Role).filter(
                models.role.Role.id == role.role_id
            ).first()
            if role_obj:
                role_info_list.append(RoleInfo(
                    id=role_obj.id,
                    name=role_obj.name
                ))
        
        # Create unit info object if unit exists
        unit_info = None
        if unit:
            unit_info = UnitInfo(
                id=unit.id,
                name=unit.name
            )
        
        # Create user response object
        user_response = UserResponse(
            id=user.id,
            username=user.username,
            is_active=user.is_active,
            roles=role_info_list,
            unit_id=unit_id,
            unit=unit_info
        )
        
        result.append(user_response)
    
    return result

@router.post("/", response_model=UserResponse)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Create new user.
    """
    user_obj = crud_user.create(db=db, obj_in=user_in)
    return user_obj

@router.put("/{id}", response_model=UserResponse)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    user_in: UserUpdate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update user.
    """
    user_obj = crud_user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    user_obj = crud_user.update(db=db, db_obj=user_obj, obj_in=user_in)
    return user_obj

@router.get("/{id}", response_model=UserResponse)
def get_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get user by ID.
    """
    user_obj = crud_user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    return user_obj

@router.delete("/{id}", response_model=UserResponse)
def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Delete user.
    """
    user_obj = crud_user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    user_obj = crud_user.remove(db=db, id=id)
    return user_obj

@router.get("/me", response_model=UserMe)
def read_user_me(
    current_user = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
):
    """
    Get current user information including units, roles and permissions
    """
    # Get user's units through UserUnit relationship
    user_units = db.query(models.user_unit.UserUnit).filter(
        models.user_unit.UserUnit.user_id == current_user.id
    ).all()
    
    units = []
    for user_unit in user_units:
        unit = db.query(models.unit.Unit).filter(
            models.unit.Unit.id == user_unit.unit_id
        ).first()
        if unit:
            units.append(unit)
    
    # Get user's roles
    roles = db.query(models.user_role.UserRole).filter(
        models.user_role.UserRole.user_id == current_user.id
    ).all()
    
    # Get user's permissions
    permissions = db.query(models.user_permission.UserPermission).filter(
        models.user_permission.UserPermission.user_id == current_user.id
    ).all()
    
    # Create response data
    user_data = current_user.__dict__
    user_data['units'] = [unit.__dict__ for unit in units] if units else []
    user_data['roles'] = [role.__dict__ for role in roles] if roles else []
    user_data['permissions'] = [permission.__dict__ for permission in permissions] if permissions else []
    
    return user_data

class UserPasswordUpdate(BaseModel):
    password: str

@router.put("/{user_id}/password")
def update_user_password(
    *,
    db: Session = Depends(deps.get_db),
    user_id: str,
    password_data: UserPasswordUpdate,
    current_user = Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update user password
    """
    user = crud_user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Generate new salt and hash password
    salt = get_salt()
    hashed_password = get_password_hash(f'{password_data.password}{salt}')
    
    # Update user
    user.salt = salt
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    
    return {"message": "Password updated successfully"}

class UserRoleUpdate(BaseModel):
    role_ids: List[UUID]

@router.put("/{user_id}/roles")
def update_user_roles(
    *,
    db: Session = Depends(deps.get_db),
    user_id: str,
    role_data: UserRoleUpdate,
    current_user = Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update user roles
    """
    user = crud_user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Remove existing roles
    db.query(models.user_role.UserRole).filter(
        models.user_role.UserRole.user_id == user_id
    ).delete()
    
    # Add new roles
    for role_id in role_data.role_ids:
        user_role = models.user_role.UserRole(
            user_id=user_id,
            role_id=role_id
        )
        db.add(user_role)
    
    db.commit()
    
    return {"message": "Roles updated successfully"}

@router.put("/{user_id}/toggle-active")
def toggle_user_active(
    *,
    db: Session = Depends(deps.get_db),
    user_id: str,
    current_user = Security(deps.get_current_active_user, scopes=[]),
):
    """
    Toggle user active state
    """
    user = crud_user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Toggle active state
    user.is_active = not user.is_active
    db.commit()
    db.refresh(user)
    
    return {"message": f"User {'activated' if user.is_active else 'deactivated'} successfully"}