import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class tinhchat_hoinhom(Base):
    """
    Database model for an tinhchat hoinhom
    """
    __tablename__='tinhchat_hoinhom'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    tinhchat_id = Column(Integer, ForeignKey('tinhchat.id'), nullable=False)
    uid= Column(String(20), ForeignKey('uid.uid'), nullable=False) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    # tinchat = relationship('tinhchat')