from fastapi import APIRouter, Depends
from app.services.loan_service import add_loan_service,get_loan_by_id_service,get_all_active_loans_service,get_loan_by_member_service,list_all_loans_service,return_loan_service,remove_loan_service
from app.schemas.request.loan import CreateLoan, LoanReturn
from app.schemas.response.loan import LoanCreated, LoanOut, LoanReturnDateUpdateResponse, RemovedLoanResponse
from app.middleware.dependencies import require_librarian_admin, require_librarian_employee
router = APIRouter()

@router.post("/loans", response_model = LoanCreated, dependencies=[Depends(require_librarian_admin)])
def create_loan(loan:CreateLoan):
    new_id = add_loan_service(loan.book_id, loan.member_id, loan.loan_date)
    return new_id
@router.get("/loans", response_model = list[LoanOut], dependencies=[Depends(require_librarian_employee)])
def get_all_loans():
    loans = list_all_loans_service()
    return loans
@router.get("/loans/active", response_model = list[LoanOut], dependencies=[Depends(require_librarian_employee)])
def get_all_active_loans():
    active_loans = get_all_active_loans_service()
    return active_loans
@router.get("/loans/{id}", response_model = LoanOut, dependencies=[Depends(require_librarian_employee)])
def get_loan_by_id(id:int):
    loan = get_loan_by_id_service(id)
    return loan
@router.get("/loans/{member_id}", response_model = list[LoanOut], dependencies=[Depends(require_librarian_employee)])
def get_loan_by_member(member_id:int):
    loan_by_member = get_loan_by_member_service(member_id)
    return loan_by_member
@router.put("/loans/{id}", response_model= LoanReturnDateUpdateResponse, dependencies=[Depends(require_librarian_employee)])
def return_loan(id:int, loan: LoanReturn):
    result = return_loan_service(id, loan.return_date, loan.book_id, loan.member_id)
    return result
@router.delete("/loans/{id}", response_model=RemovedLoanResponse, dependencies=[Depends(require_librarian_admin)])
def remove_loan(id:int):
    result = remove_loan_service(id)
    return result