from pydantic import BaseModel, Field
from typing import optional 
from datetime import datetime

class BookingBase(BaseModel):

    """
        shared properties for a booking.
    """

    user_id: int = Field(..., description="The id of the user making the booking .")
    slot_id: int = Field(...,description="The ID of the parking slot being booked.")
    price: float = Field(...,description="The price of the booking.")

class BookingCreate(BookingBase):

    """
        properties required for creating a booking .
        
    """
    pass # inherits all fields from BookingBase

class BookingUpdate(BaseModel):

    """
        properties that can be updated in the booking
    """
    price: optional[float] = Field(None, description="updated price of the booking.")
    status: optional[str] = Field(None, description="updated status of the booking (e.g active, canceled )")

class BookingResponse(BookingBase):

    """
         properties returned when fetching a booking.
    """

    id: int = Field(...,description="Unique identifier for the booking.")
    created_at: datetime = Field(...,description="Timestamp when the booking was created.")

    class Config:
        class Config:
            from_attributes = True
