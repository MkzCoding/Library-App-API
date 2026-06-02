from pydantic import BaseModel, Field

class UserRegistration(BaseModel):
    name: str
    email: str
    username: str
    password: str = Field(min_length=8)
    usertype: str