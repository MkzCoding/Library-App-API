from pydantic import BaseModel
from datetime import date

class Loan(BaseModel):
    id: int
    book_id: int
    member_id: int
    loan_date: date
    return_date: date | None = None