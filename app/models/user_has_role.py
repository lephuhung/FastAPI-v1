import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class user_has_role(Base):
    """
    Database model for an user_has_role
    """

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    uid_facebook = Column(String(20), ForeignKey('uid.uid'), nullable=False) 
    moiquanhe_id = Column(String(20), ForeignKey('moiquanhe.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    moiquanhe = relationship("moiquanhe", back_populates="quantrivien")