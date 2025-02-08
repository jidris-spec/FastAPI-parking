from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.session import get_db
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserUpdate, UserResponse,ForgotPasswordRequest, ResetPasswordRequest
from sqlalchemy import text
from app.utils.token_utils import create_reset_token, verify_reset_token
from app.utils.email import send_reset_email
from app.utils.email import send_email

router = APIRouter() 

@router.post("/", response_model=UserResponse, summary="Create a new user")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # db.execute(text("drop table if exists users"))
    # db.execute(text("drop table if exists user"))
    # db.execute(text("drop table if exists slots"))
    # db.execute(text("drop table if exists slot"))
    # db.execute(text("drop table if exists bookings"))
    # db.execute(text("drop table if exists booking"))
    # db.execute(text("drop table if exists parking_lots"))
    user_service = UserService(db)
    return user_service.create_user(user_data)

@router.get("/", response_model=list[UserResponse], summary="Get all users")
def list_users(db: Session = Depends(get_db)):
    user_service =UserService(db)
    return user_service.get_all_users()

@router.patch("/{user_id}", response_model=UserResponse, summary="update user with id")
def update_user(user_id:int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.update_user( user_id, user_data)

@router.get("/{user_id}", response_model=UserResponse, summary="Get user by id")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_user_by_id(user_id)
@router.post("/forgot-password/", summary="Send password reset email")
def forgot_password(email: str, db: Session = Depends(get_db)):
    # Check if the user exists
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Generate a reset token
    token = create_reset_token(user.email)
    
    # Store the reset token in the user model
    user.reset_token = token
    db.commit()
    
    # Send the reset email with a link (adjust the URL as needed)
    send_reset_email(user.email, token)
    
    return {"message": "Password reset email sent"} 

# def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
#     return UserService.request_password_reset(db, request.email)

@router.post("/reset-password", summary="Reset user password")
def reset_password_api(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    user_service = UserService(db)  # ✅ Create an instance
    return user_service.reset_password(request.token, request.new_password)  # ✅ Pass correct parameters
