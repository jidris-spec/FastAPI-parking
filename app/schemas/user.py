# app/schemas/user.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    """
    Shared properties for user data across requests and responses.
    """
    email: EmailStr = Field(..., description="User's email address.")

class UserCreate(UserBase):
    """
    Properties required for creating a new user.
    """
    password: str = Field(..., min_length=8, description="User's password.")
    username: str = Field(..., description="User's username.")
    phone: str = Field(..., description="user's phone number")
class UserResponse(UserBase):
    """
    Properties returned in response to user-related endpoints.
    """
    id: int = Field(..., description="Unique identifier of the user.")
    is_admin: bool = Field(..., description="Indicates if the user's account is active.")

class UserLogin(UserBase):
    """
    Properties required for logging in a  user.
    """
    password: str = Field(..., min_length=8, description="User's password.")
    
    class Config:
        orm_mode = True  # Enables compatibility with ORM objects.