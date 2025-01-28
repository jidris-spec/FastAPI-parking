from pydantic import BaseModel, Field
from typing import Optional


class SlotBase(BaseModel):
    """
    Shared properties for parking slots.
    """
    slot_number: str = Field(..., description="The unique identifier for the parking slot.")
    is_available: bool = Field(..., description="Indicates if the parking slot is currently available.")
    lot_id: int = Field(..., description="ID of the parking lot where this slot belongs.")


class SlotCreate(SlotBase):
    """
    Properties required for creating a new parking slot.
    """
    pass  # Inherits all fields from SlotBase; additional fields can be added if needed.


class SlotUpdate(BaseModel):
    """
    Properties for updating a parking slot.
    """
    is_available: Optional[bool] = Field(None, description="Update the availability of the slot.")


class SlotResponse(SlotBase):
    """
    Properties returned in response to slot-related endpoints.
    """
    id: int = Field(..., description="Unique identifier of the parking slot.")
    
    class Config:
        orm_mode = True  # Enables compatibility with ORM objects.
