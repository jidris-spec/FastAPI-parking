from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class Slot(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(Boolean, default=True)
    price = Column(Integer)
    location = Column(String)