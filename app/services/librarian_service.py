from app.db.librarian_repo import add_librarian, get_librarian_by_id, get_librarian_by_username, get_all_librarians, update_librarian_email, update_librarian_role,delete_librarian
from fastapi import HTTPException
from app.utils.security import hash_password
def add_librarian_service(librarian_name, librarian_email, user_role, librarian_username, librarian_password):
    existing = get_librarian_by_username(librarian_username)
    if existing:
        raise HTTPException(
            status_code=409,
            detail="User already exists."
        )
    librarian_hashed_password = hash_password(librarian_password)
    librarian_role = "admin" if user_role == "librarian-admin" else "employee"
    add_librarian(librarian_name, librarian_email, librarian_role, librarian_username, librarian_hashed_password)
    return {"username":librarian_username, "message":"Registration Successful.", "role":librarian_role}

def remove_librarian_service(librarian_id):
    existing = get_librarian_by_id(librarian_id)
    if existing:
        row_deleted = delete_librarian(librarian_id)
        return {"success": row_deleted > 0, "message":"Librarian removed" if row_deleted else "No librarian deleted."}
    else:
       raise HTTPException(
           status_code=404,
           detail="Librarian not found."
       )
    
def get_librarian_by_id_service(librarian_id):
    existing = get_librarian_by_id(librarian_id)
    if existing:
        return existing
    else:
        raise HTTPException(
            status_code=404,
            detail="Librarian not found."
        )

def list_librarians_service():
    librarians = get_all_librarians()
    if not librarians:
        raise HTTPException(
            status_code=404,
            detail="No librarians found."
        )
    return librarians

def update_librarian_email_service(librarian_id, librarian_email):
    existing = get_librarian_by_id(librarian_id)
    if existing:
        update_librarian_email(librarian_id, librarian_email)
        return {"success":True, "message":"Librarian email has been updated."}
    else:
        raise HTTPException(
            status_code=404,
            detail="Librarian not found."
        )
    
def update_librarian_role_service(librarian_id, librarian_role):
    existing = get_librarian_by_id(librarian_id)
    if existing:
        update_librarian_role(librarian_id, librarian_role)
        return {"success":True, "message":"Librarian role has been updated."}
    else:
        raise HTTPException(
            status_code= 404,
            detail="Librarian not found."
        )
    
def remove_librarian_service(librarian_id):
    existing = get_librarian_by_id(librarian_id)
    if existing:
        row_deleted = delete_librarian(librarian_id)
        return {"success": row_deleted > 0, "message":f"Librarian removed" if row_deleted else "No librarian removed."}
    else:
        raise HTTPException(
            status_code= 404,
            detail="Librarian not found."
        )