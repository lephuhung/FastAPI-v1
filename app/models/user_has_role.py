import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class user_has_role(Base):
    """
    Database model for an user_has_role
    """
    __tablename__='user_has_role'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    user_id = Column(UUID(as_uuid=True),ForeignKey("user.id"),primary_key=True,nullable=False)
    role_id = Column(UUID(as_uuid=True),ForeignKey("Role.id"),primary_key=True,nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )