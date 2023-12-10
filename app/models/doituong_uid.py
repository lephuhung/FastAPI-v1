import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Doituong_UID(Base):
    """
    Database model for an Doituong UUID
    """

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    doituong_id = Column(Integer, ForeignKey("doituong.id"))
    uid = Column(String(20) )
    moiquanhe_id= Column(Integer, ForeignKey("moiquanhe.id"))
    color = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    color= relationship("moiquanhe", back_populated="doituong_uid")