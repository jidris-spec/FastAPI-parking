from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserUpdate
from datetime import datetime, timedelta
import secrets
from app.utils.utils import hash_password  

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
    
    def generate_reset_token():
        return secrets.token_urlsafe(32)
        
@staticmethod    
def set_reset_token(db: Session, user: User): # Store Reset Token in Database
        token = UserRepository.generate_reset_token()
        user.reset_token = token
        user.reset_token_expiry = datetime.utcnow() + timedelta(minutes=10)
        db.commit()
        return token


def verify_reset_token(db: Session, token: str):
        user = db.query(User).filter(User.reset_token ==token).first()
        if user and user.reset_token_expiry > datetime.utcnow():
            return user
        return None

def update_password(db: Session, user: User, new_password: str):
        user.hashed_password = hash_password(new_password)
        user.reset_token = None 
        user.reset_token_expiry = None
        db.commit()
    
    

    