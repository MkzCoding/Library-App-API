from fastapi import APIRouter, HTTPException
from typing import Union
from app.schemas.request.registration_request import UserRegistration
from app.services.member_services import add_member_service
from app.services.librarian_service import add_librarian_service
from app.schemas.response.member import MemberCreated
from app.schemas.response.librarian import CreatedLibrarian
router = APIRouter()

@router.post("/registration", response_model = Union[MemberCreated, CreatedLibrarian])
def create_user(user: UserRegistration):
    if user.usertype.lower() == "member":
        new_member = add_member_service(user.name, user.email, user.username, user.password)
        return MemberCreated(**new_member)
    elif user.usertype.lower() == "librarian-admin":
        new_librarian = add_librarian_service(user.name, user.email, user.usertype, user.username, user.password)
        return CreatedLibrarian(**new_librarian)
    elif user.usertype.lower() == "librarian-employee":
        new_librarian = add_librarian_service(user.name, user.email, user.usertype, user.username, user.password)
        return CreatedLibrarian(**new_librarian)
    else:
        raise HTTPException(
            status_code=403,
            detail="Invalid user type."
        )
