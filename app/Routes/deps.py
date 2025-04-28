import logging
from typing import Generator, Optional
from pydantic import UUID4
from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.schemas.access_token import AccessTokenData

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/access-token",
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    security_scopes: SecurityScopes,
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2),
) -> models.user.User:

    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials test1",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        if payload.get("username") is None:
            raise credentials_exception
        token_data = AccessTokenData(**payload)
    except (jwt.JWTError, ValidationError) as e:
        logger.error(f"Token validation failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials test 403",
        )
    user = crud.crud_user.get(db, token_data.id)

    print(f"[DEBUG] User ID: {token_data.id}")
    print(f"[DEBUG] User Role: {token_data.role}")
    print(f"[DEBUG] User Permissions: {token_data.permissions}")
    print(f"[DEBUG] User: {user}")
    if not user:
        raise credentials_exception
    if security_scopes.scopes and not token_data.role:
        raise HTTPException(
            status_code=401,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": authenticate_value},
        )
    for scope in security_scopes.scopes:
        if check_permission_in_role(scope, role_id=token_data.role[0], db=db):
            return user
    if security_scopes.scopes == []:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not enough permissions",
        headers={"WWW-Authenticate": authenticate_value},
    )


def get_current_active_user(
    current_user: models.user.User = Security(get_current_user, scopes=[]),
) -> models.user.User:
    print(f"[DEBUG] Current user: {current_user.username}")
    if not crud.crud_user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def check_permission_in_role(permission_id: str, role_id: UUID4, db: Session):
    role_permission = crud.role_permission.get_by_role_and_permission(
        db=db, role_id=role_id, permission_id=permission_id
    )
    return role_permission is not None


def check_access_permission(user_id: UUID4, unit_id: UUID4, db: Session):
    # Lấy vai trò của người dùng
    user_roles = crud.user_role.get_by_user_id(db=db, user_id=user_id)
    if not user_roles:
        return False
        
    # Nếu là superadmin thì có quyền truy cập tất cả
    for user_role in user_roles:
        role = crud.role.get(db=db, id=user_role.role_id)
        if role and role.name == "superadmin":
            return True
        
    # Nếu là admin thì chỉ có quyền truy cập đơn vị của mình
    for user_role in user_roles:
        role = crud.role.get(db=db, id=user_role.role_id)
        if role and role.name == "admin":
            user = crud.user.get(db=db, id=user_id)
            if not user or not user.unit_id:
                return False
            return user.unit_id == unit_id
        
    return False


def get_current_user_with_access(
    current_user: models.user.User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> models.user.User:
    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )
    return current_user


def check_unit_access(
    unit_id: UUID4,
    current_user: models.user.User = Depends(get_current_user_with_access),
    db: Session = Depends(get_db)
):
    if not check_access_permission(current_user.id, unit_id, db):
        raise HTTPException(
            status_code=403,
            detail="Not enough permissions"
        )
    return True


def get_current_superadmin(
    current_user: models.user.User = Depends(get_current_active_user),
) -> models.user.User:
    if not current_user.is_superadmin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    return current_user