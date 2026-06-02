from pydantic import BaseModel

class UserLogIn(BaseModel):
    username: str
    password: str
