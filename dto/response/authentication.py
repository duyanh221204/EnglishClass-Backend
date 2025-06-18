from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenDataResponse(BaseModel):
    id: int
    jti: str
