from pydantic import BaseModel, EmailStr, Field


class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str = Field(pattern=r"^0\d{9}$")
