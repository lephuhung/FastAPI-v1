import logging
from typing import Generator
from pydantic import UUID4
from app import crud, models, schemas
from app.constants.role import Role
from app.core import sercurity
from app.core.config import settings
from app.db.session import SessionLocal
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt
from app.models.role_has_permission import Role_has_permission
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.schemas.access_token import AccessTokenData
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/access-token",
    # scopes={
    #     Role.GUEST["name"]: Role.GUEST["description"],
    #     Role.ACCOUNT_ADMIN["name"]: Role.ACCOUNT_ADMIN["description"],
    #     Role.ACCOUNT_MANAGER["name"]: Role.ACCOUNT_MANAGER["description"],
    #     Role.ADMIN["name"]: Role.ADMIN["description"],
    #     Role.SUPER_ADMIN["name"]: Role.SUPER_ADMIN["description"],
    # },
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
) -> models.user:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        if payload.get("username") is None:
            raise credentials_exception
        token_data = AccessTokenData(**payload)
    except (jwt.JWTError, ValidationError):
        logger.error("Error Decoding Token", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.crud_user.get(db, token_data.id)
    if not user:
        raise credentials_exception
    if security_scopes.scopes and not token_data.role:
        raise HTTPException(
            status_code=401,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": authenticate_value},
        )
    for scope in security_scopes.scopes:
        print(scope)
        print(token_data.role[0])
        if check_permission_in_role(scope, role_id=token_data.role[0], db=db):
            return user
    raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )


def get_current_active_user(
    current_user: schemas.user.UserCreate = Security(get_current_user, scopes=[],),
) -> models.user:
    if not crud.crud_user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def check_permission_in_role(permission_id: str, role_id: UUID4, db: Session):
    data =db.query(Role_has_permission).filter(Role_has_permission.role_id==role_id, Role_has_permission.permission_id==permission_id).first()
    if data is None:
        return False
    return True