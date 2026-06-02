from pydantic import BaseModel
from datetime import date
class Member(BaseModel):
    id: int
    name: str
    email: str
    membership_date: date
    loan_count: int = 0
    username: str
    hashed_password: str