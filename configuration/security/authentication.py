from datetime import datetime, timezone, timedelta
from uuid import uuid4

from fastapi import Depends
from jose import jwt

from configuration.security.oauth2.cookie import OAuth2PasswordBearerCookie
from model import User
from util.constant import Constant

SECRET_KEY = Constant.SECRET_KEY
ALGORITHM = Constant.ALGORITHM
ACCESS_TOKEN_EXPIRED_MINUTES = int(Constant.ACCESS_TOKEN_EXPIRED_MINUTES)

oauth2_scheme = OAuth2PasswordBearerCookie(token_url="/api/auth/login", cookie_name="access_token")


class AuthenticationConfig:
    @staticmethod
    def create_access_token(user: User) -> str:
        to_encode = {
            "sub": str(user.id),
            "id": str(uuid4())
        }
        expired_at = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRED_MINUTES)
    
        to_encode.update({"exp": expired_at})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
