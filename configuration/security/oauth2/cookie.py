from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from starlette.requests import Request


class OAuth2PasswordBearerCookie(OAuth2PasswordBearer):
    def __init__(self, token_url: str, cookie_name: str, scheme_name: str | None = None):
        super().__init__(
            tokenUrl=token_url,
            scheme_name=scheme_name,
            auto_error=False,
        )
        self.cookie_name = cookie_name

    async def __call__(self, request: Request) -> str | HTTPException:
        cookie: str = request.cookies.get(self.cookie_name) or ""
        scheme, _, token = cookie.partition(" ")

        if not token or scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return token
