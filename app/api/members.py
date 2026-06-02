from fastapi import APIRouter, Depends
from app.services.member_services import add_member_service, get_member_by_id_service,list_all_members_service,update_member_email_service,update_member_membership_service,remove_member_service
from app.schemas.request.member import CreateMember, MemberEmailUpdate, MemberMembershipUpdate
from app.schemas.response.member import MemberCreated, MemberOut, MemberEmailUpdateResponse, MemberMembershipUpdateResponse, RemovedMember
from app.middleware.dependencies import require_librarian_admin, require_librarian_employee
router = APIRouter()

@router.post("/members", response_model= MemberCreated, dependencies=[Depends(require_librarian_admin)])
def create_member(member: CreateMember):
    new_member = add_member_service(member.name, member.email, member.membership_date, member.username, member.password)
    return (new_member["username"], new_member["message"])
@router.get("/members", response_model= list[MemberOut], dependencies=[Depends(require_librarian_admin)])
def get_all_members():
    members = list_all_members_service()
    return members
@router.get("/members/{id}", response_model= MemberOut, dependencies=[Depends(require_librarian_employee)])
def get_member_by_id(id:int):
    member = get_member_by_id_service(id)
    return member
@router.put("/members/{id}/email", response_model= MemberEmailUpdateResponse, dependencies=[Depends(require_librarian_employee)])
def update_member_email(id:int, member:MemberEmailUpdate):
    result = update_member_email_service(id, member.email)
    return result
@router.put("/members/{id}/membership", response_model= MemberMembershipUpdateResponse, dependencies=[Depends(require_librarian_employee)])
def update_member_membership(id:int, member:MemberMembershipUpdate):
    result = update_member_membership_service(id, member.membership_date)
    return result
@router.delete("/members/{id}", response_model= RemovedMember, dependencies=[Depends(require_librarian_admin)])
def remove_member(id:int):
    result = remove_member_service(id)
    return result
