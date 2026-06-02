from pydantic import BaseModel, Field
from datetime import date
class CreateMember(BaseModel):
    name:str
    email:str
    membership_date: date
    username: str 
    password: str = Field(min_length=8)

class MemberEmailUpdate(BaseModel):
    email:str

class MemberMembershipUpdate(BaseModel):
    membership_date:date