import logging
from datetime import datetime, timezone, timedelta
from typing import Annotated
from uuid import uuid4

from fastapi import Depends, HTTPException
from jose import jwt
from starlette import status

from configuration.security.oauth2.cookie import OAuth2PasswordBearerCookie
from dto.response.authentication import TokenDataResponse
from model import User
from repository.invalidated_token import InvalidatedTokenRepository, get_invalidated_token_repo
from util.constant import Constant

SECRET_KEY = Constant.SECRET_KEY
ALGORITHM = Constant.ALGORITHM
ACCESS_TOKEN_EXPIRED_MINUTES = int(Constant.ACCESS_TOKEN_EXPIRED_MINUTES)

oauth2_scheme = OAuth2PasswordBearerCookie(token_url="/api/auth/login", cookie_name="access_token")

token_dependency = Annotated[str, Depends(oauth2_scheme)]
invalidated_token_repo_dependency = Annotated[InvalidatedTokenRepository, Depends(get_invalidated_token_repo)]


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

    @staticmethod
    async def verify_token(
            token: str,
            invalidated_token_repo: InvalidatedTokenRepository
    ) -> TokenDataResponse | HTTPException:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            user_id: str = payload.get("sub")
            jti: str = payload.get("id")
            if user_id is None or jti is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials"
                )

            existed_jti = await invalidated_token_repo.find_by_id(jti)
            if existed_jti is not None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials"
                )

            return TokenDataResponse(id=int(user_id), jti=jti)

        except Exception as e:
            logging.error (f"Cannot verify token: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )

    @staticmethod
    async def get_current_user(
            token: token_dependency,
            invalidated_token_repo: invalidated_token_repo_dependency
    ) -> TokenDataResponse | HTTPException:
        return await AuthenticationConfig.verify_token(token, invalidated_token_repo)
