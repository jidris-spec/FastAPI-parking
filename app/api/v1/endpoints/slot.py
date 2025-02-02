from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models.slot import Slot
from app.schemas.slot import SlotCreate, SlotResponse

router = APIRouter()

@router.post("/", response_model=SlotResponse, summary="Create a new parking slot")
async def create_slot(slot_data: SlotCreate, db: AsyncSession = Depends(get_db)):
    # Check if a slot with the same identifier already exists (optional validation)
    existing_slot = await db.execute(select(Slot).filter(Slot.identifier == slot_data.identifier))
    if existing_slot.scalars().first():
        raise HTTPException(status_code=400, detail="A slot with this identifier already exists")
    
    # Create a new parking slot
    new_slot = Slot(
        identifier=slot_data.identifier,
        is_available=True,  # Default to available
        price_per_hour=slot_data.price_per_hour
    )
    db.add(new_slot)
    await db.flush()
    await db.commit()
    await db.refresh(new_slot)
    return new_slot

@router.get("/", response_model=list[SlotResponse], summary="List all parking slots")
async def list_slots(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Slot))
    slots = result.scalars().all()
    return slots
