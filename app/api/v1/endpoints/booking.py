from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models.booking import Booking
from app.db.models.user import User
from app.db.models.slot import Slot  # Ensure the correct model name is imported
from app.schemas.booking import BookingCreate, BookingResponse

router = APIRouter()

@router.post("/", response_model=BookingResponse, summary="Create a new booking")
async def create_booking(booking: BookingCreate, db: AsyncSession = Depends(get_db)):
    # Check if the user exists
    user_result = await db.execute(select(User).filter(User.id == booking.user_id))
    user = user_result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the slot exists and is available
    slot_result = await db.execute(
        select(Slot).filter(Slot.id == booking.slot_id, Slot.is_available == True)
    )
    slot = slot_result.scalars().first()
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found or not available")

    # Create a new booking
    new_booking = Booking(
        user_id=booking.user_id,
        slot_id=booking.slot_id,
        price=booking.price,
    )
    db.add(new_booking)

    # Mark the parking slot as unavailable
    slot.is_available = False

    await db.commit()
    await db.refresh(new_booking)
    return new_booking

@router.get("/", response_model=list[BookingResponse], summary="List all bookings")
async def list_bookings(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Booking))
    bookings = result.scalars().all()
    return bookings
