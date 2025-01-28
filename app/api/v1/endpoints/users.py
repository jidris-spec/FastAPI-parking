from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.user_service import UserService
from app.schemas.user import UserResponse, UserCreate, UserLogin

router = APIRouter()

@router.post("/register/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user_data)

@router.post("/login/", response_model=UserResponse)

def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.login_user(user_data)