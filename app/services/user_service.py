# app/services/user_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin,UserUpdate
from app.core.security import hash_password, verify_password, create_access_token
from app.utils.email import send_email
# from utils import send_email
class UserService:
    def __init__(self, db: Session): 
        self.user_repository = UserRepository(db)

    def create_user(self, user_data: UserCreate):
        print(user_data)
        existing_user = self.user_repository.get_user_by_email(user_data.email)
        print(existing_user)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        hashed_password = hash_password(user_data.password)
        user = self.user_repository.create_user(
            email=user_data.email,
            hashed_password=hashed_password,
            username=user_data.username,
            phone=user_data.phone
        )

        return user

    def login_user(self, user_data: UserLogin):
        user = self.user_repository.get_user_by_email(user_data.email)
        if not user:
            raise ValueError("Invalid email or password")
        if not verify_password(user_data.password, user.hashed_password):
            raise ValueError("Invalid email or password")
        print(user)
        data={
            "email":user.email,
            "username":user.username,
            "is_admin":user.is_admin,
            "phone":user.phone,
            "id":user.id
            }
        access_token = create_access_token(data=data
        )
        return {"access_token": access_token, "token_type": "bearer"}

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)

    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)
    
    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def update_user(self,user_id:int,user_data:UserUpdate):
        user = self.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        user = self.user_repository.update_user(
        phone=user_data.phone,
        is_admin=user_data.is_admin,
        username=user_data.username,
        user_id=user_id
        )
        return user
    def request_password_reset(self, db: Session, email: str):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")  
        
        token = UserRepository.set_reset_token(db, user)
        reset_link = f"http://localhost:8000/reset-password?token={token}"
        send_email(user.email, "password Rest", f"Click the link to reset your password: {reset_link}")
        return {"message": "password reset link has been sent to your email"}
    
    def reset_password(self, db: Session, token: str, new_password: str):
        user = UserRepository.verify_reset_token(db, token) 
        if not user:
            raise HTTPException(status_code=400, detail="Invalid or expires token")
        
        UserRepository.update_password(db, user, new_password)
        return {"message": "password reset successfully"}
