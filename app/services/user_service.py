# app/services/user_service.py
from sqlalchemy.orm import Session
from app.db.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token
from app.utils.email import send_email

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

        # Send welcome email
        # send_email("Welcome to jidtech Car Parking System!", user.email, "Thank you for registering.")
        print(user)
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
