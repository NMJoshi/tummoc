from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
# For Hashing Password
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(hashed_password, user_password):
        return pwd_context.verify(user_password, hashed_password)


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "aa027dd528d9fcad7ff142986c7f5d1a4087fad7353b1e47d9aafed1d9272778"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 2


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        message: str = payload.get("message")
        if message is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return message
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
