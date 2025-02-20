from sqlalchemy import create_engine, Column , Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PasswordResetToken(Base):
    __tablename__ = "password_reset_token"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    token = Column(String, nullable = False)
    created_at = Column(DateTime, default=func.now())
    expires_at = Column(DateTime, nullable=False)
engine = create_engine("sqlite:///parking.db")
Base.metadata.create_all(engine)

print("Table 'password_reset_tokens' created successfully!")


