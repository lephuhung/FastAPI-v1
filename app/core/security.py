from datetime import datetime, timedelta
from typing import Any, Union
import secrets
import string
from app.core.config import settings
from jose import jwt
from passlib.context import CryptContext
from app import schemas, models, crud
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, **subject}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=ALGORITHM
    )
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for i in range(length))
    return random_string
    
def get_salt()->str:
    salt= generate_random_string()
    return salt

def authenticate_user(username: str, password:str, db: Session):
    user = crud.crud_user.get_by_name(db=db, username=username)
    if not user:
        return False
    if not verify_password(f'{password}{user.salt}', user.password):
        return False
    return user