from pydantic import BaseModel
from datetime import date
from typing import Optional
class CreateLoan(BaseModel):
    book_id:int
    member_id:int
    loan_date: date

class LoanReturn(BaseModel):
    return_date:date
    book_id:int
    member_id:int
   