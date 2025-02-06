from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    slot_id = Column(Integer, ForeignKey("slots.id"))
    price = Column(Integer)
    status = Column(String, default="active", nullable=False)
