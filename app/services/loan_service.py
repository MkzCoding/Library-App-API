from app.db.loan_repo import add_loan, delete_loan, get_active_loans, get_all_loans,get_loan_by_id, get_loans_by_member, return_loan
from app.db.member_repo import update_member_loan_count, get_member_by_id
from app.db.book_repo import get_book_by_id, update_book_availability
from fastapi import HTTPException
def add_loan_service(book_id, member_id, loan_date):
    book  = get_book_by_id(book_id)
    book_available = book.available
    member = get_member_by_id(member_id)
    if not book or not member:
        raise HTTPException(
            status_code=404,
            detail="Book or Member not found."
        )
    if book_available == 1:
        if member.loan_count < 3:
            new_id = add_loan(book_id, member_id, loan_date)
            update_member_loan_count(member_id, member.loan_count +1)
            update_book_availability(book_id, 0)
            return {"success":True, "message":f"Loan: {new_id} has been added."}
        raise HTTPException(
            status_code=409,
            detail="Loans limit reached."
        )
    else:
        raise HTTPException(
            status_code=409,
            detail="Book currently unavailable."
        )

def return_loan_service(loan_id, return_date, book_id, member_id):
    result  = get_loan_by_id(loan_id)
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Loan not found."
        )
    return_loan(loan_id, return_date)
    update_book_availability(book_id,1)
    member = get_member_by_id(member_id)
    update_member_loan_count(member_id, member.loan_count - 1)
    return {"success":True, "message":"Loan returned."}

def get_loan_by_id_service(loan_id):
    existing = get_loan_by_id(loan_id)
    if existing:
        return existing
    else:
        raise HTTPException(
            status_code= 404,
            detail="Loan not found."
        )

def get_loan_by_member_service(member_id):
    loans = get_loans_by_member(member_id)
    if not loans:
        raise HTTPException(
            status_code=404,
            detail="No loans found."
        )
    return loans
def list_all_loans_service():
    loans = get_all_loans()
    if not loans:
        raise HTTPException(
            status_code=404,
            detail="No loans found."
        )
    return loans

def get_all_active_loans_service():
    active_loans = get_active_loans()
    if not active_loans:
        raise HTTPException(
            status_code=404,
            detail="No active loans found."
        )
    return active_loans

def remove_loan_service(loan_id):
    deleted_loan = delete_loan(loan_id)
    if deleted_loan:
        return {"success":True, "message":"Loan deleted"}
    else:
        raise HTTPException(
            status_code=404,
            detail="Loan not found."
        )
    