import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class trichtin(Base):
    """
    Database model for an uid
    """

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    uid = Column(String(20), ForeignKey('uid.uid'), nullable=False)
    ghichu_noidung = Column(String(1000), ForeignKey('uid.uid'), nullable=False) 
    nhanxet = Column(String(255), nullable= True)
    xuly= Column(String(255))
    uid_vaiao = Column(String(20), nullable= False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )