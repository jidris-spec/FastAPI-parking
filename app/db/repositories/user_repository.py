from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserUpdate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email: str, hashed_password: str, username: str, phone: str) -> User:
        user = User(email=email, hashed_password=hashed_password, username=username, phone=phone)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_all_users(self):
        return self.db.query(User).all()
    
    def update_user(self,user_id:int, phone: str, is_admin: bool, username:str) -> User:
        user = self.get_user_by_id(user_id)
        if user:
            if phone is not None:
                user.phone =phone
            if is_admin is not None:
                user.is_admin = is_admin
            if username is not None:
                user.username = username
            self.db.commit()
            self.db.refresh(user)
            return user
        else:
            return None  # Handle case where user doesn't exist.