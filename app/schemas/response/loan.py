from pydantic import BaseModel
from datetime import date
class LoanCreated(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True

class LoanOut(BaseModel):
    id: int
    book_id: int
    member_id: int
    loan_date: date
    return_date: date | None = None

    class Config:
        orm_mode = True

class LoanReturnDateUpdateResponse(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True

class RemovedLoanResponse(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True