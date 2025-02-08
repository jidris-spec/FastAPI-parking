from datetime import datetime, timedelta
from jose import JWTError, jwt

# Make sure to use a secure secret key in production
SECRET_KEY = "your-secret-key"  
ALGORITHM = "HS256"
RESET_TOKEN_EXPIRE_MINUTES = 15  # Token expires after 15 minutes

def create_reset_token(email: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    data = {"sub": email, "exp": expire}
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_reset_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None
