from pydantic import BaseModel


class TokenCreateResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
