import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class UID(Base):
    """
    Database model for an uid
    """

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String(20))
    name = Column(String(255))
    reaction = Column(Integer)
    SDT = Column(String(10), default=Nullable)
    trangthai_id = Column(Integer, ForeignKey('trangthai.id'))
    type_id = Column(Integer, ForeignKey('type.id'))
    ghichu = Column(String(5000), default=Nullable)
    Vaiao= Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    # models = relationship("", back_populates="account")