from app.db.member_repo import add_member, get_member_by_username, get_member_by_id, get_all_members, update_member_email, update_member_membership, delete_member
from fastapi import HTTPException
from app.utils.security import hash_password
from datetime import date
def add_member_service(member_name, member_email, member_username, member_password):
    existing = get_member_by_username(member_username)
    if existing:
        raise HTTPException(
            status_code=409,
            detail="User already exists."
        )
    hashed_password = hash_password(member_password)
    member_membership_date = date.today()
    add_member(member_name, member_email, member_membership_date, member_username, hashed_password)
    return {"username":member_username, "message":"Registration successful."}

def remove_member_service(member_id):
    existing = get_member_by_id(member_id)
    if existing:
        if existing.loan_count > 0:
            raise HTTPException(
                status_code=409,
                detail="Member has active loans and cannot be deleted."
            )
        deleted_row = delete_member(member_id)
        return {"success": deleted_row > 0, "message":"Member deleted" if deleted_row else "No member was deleted."}
    else:
        raise HTTPException(
            status_code=404,
            detail="Member not found."
        )

def get_member_by_id_service(member_id):
    existing = get_member_by_id(member_id)
    if existing:
        return existing
    else:
        raise HTTPException(
            status_code=404,
            detail="Member not found."
        )
def list_all_members_service():
    members = get_all_members()
    if not members:
        raise HTTPException(
            status_code=404,
            detail="No members found."
        )
    return members

def update_member_email_service(member_id, member_email):
    existing = get_member_by_id(member_id)
    if existing:
        update_member_email(member_id, member_email)
        return {"success":True, "message":"Member email updated."}
    else:
        raise HTTPException(
            status_code= 404,
            detail="Member not found."
        )

def update_member_membership_service(member_id, member_membership_date):
    existing = get_member_by_id(member_id)
    if existing:
        update_member_membership(member_id, member_membership_date)
        return {"success":True, "message":"Member membership updated."}
    else:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

