from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET = "SUA_KEY_AQUI"  # depois coloque no .env
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(days=7)
    return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM) 
