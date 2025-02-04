from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from sqlalchemy import text

router = APIRouter() 

@router.post("/", response_model=UserResponse, summary="Create a new user")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    db.execute(text("drop table if exists users"))
    db.execute(text("drop table if exists user"))
    db.execute(text("drop table if exists slots"))
    db.execute(text("drop table if exists slot"))
    db.execute(text("drop table if exists bookings"))
    db.execute(text("drop table if exists booking"))
    db.execute(text("drop table if exists parking_lots"))
    user_service = UserService(db)
    return user_service.create_user(user_data)

@router.get("/", response_model=list[UserResponse], summary="Get all users")
def list_users(db: Session = Depends(get_db)):
    user_service =UserService(db)
    return user_service.get_all_users()

@router.put("/{user_id}", response_model=UserResponse, summary="update user with id")
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.update_user(user_id, user_data)

@router.get("/{user_id}", response_model=UserResponse, summary="Get user by id")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_user_by_id(user_id)

   