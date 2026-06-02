from pydantic import BaseModel
from datetime import date

class MemberCreated(BaseModel):
    username: str
    message: str

    class Config:
        orm_mode = True

class MemberOut(BaseModel):
    username: str
    membership_date: date
    loan_count : int

    class Config:
        orm_mode = True

class MemberEmailUpdateResponse(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True

class MemberMembershipUpdateResponse(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True

class RemovedMember(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True