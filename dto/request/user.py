from pydantic import BaseModel, EmailStr, Field


class UserInfoCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str = Field(pattern=r"^0\d{9}$")
    avatar: str | None = None


class UserAuthCreateRequest(BaseModel):
    username: str
    password: str = Field(min_length=8, max_length=15)
