from pydantic import BaseModel

class UserLogInResponse(BaseModel):
    username: str
    message: str

    class ConfigDict:
        orm_mode = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

    class ConfigDict:
        orm_mode = True