from datetime import datetime, timezone, timedelta
from uuid import uuid4

from jose import jwt
from passlib.context import CryptContext

from util.constant import Constant


class AuthenticationConfig:
    def __init__(self):
        self.secret_key = Constant.SECRET_KEY
        self.algorithm = Constant.ALGORITHM
        self.access_token_expired_minutes = int(Constant.ACCESS_TOKEN_EXPIRED_MINUTES)
        self.bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, plain_password: str) -> str:
        return self.bcrypt_context.hash(plain_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.bcrypt_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        jwt_id = str(uuid4())
        expired_at = datetime.now(timezone.utc) + timedelta(minutes=self.access_token_expired_minutes)

        to_encode.update(
            {
                "exp": expired_at,
                "id": jwt_id
            }
        )
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
