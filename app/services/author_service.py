from app.db.author_repo import add_author, get_author_by_id, get_all_authors, delete_author
from fastapi import HTTPException
def add_author_service(author_name, author_nationality):
    new_id = add_author(author_name, author_nationality)
    return {"success":True,"author_id":new_id}

def remove_author_service(author_id):
    existing = get_author_by_id(author_id)
    if existing:
        deleted_row = delete_author(author_id)
        return {"success": deleted_row > 0, "message":"Author removed." if deleted_row else "No Author deleted."}
    else:
        raise HTTPException(
            status_code=404,
            detail="Author not found."
        )
    
def get_author_by_id_service(author_id):
    existing = get_author_by_id(author_id)
    if existing:
        return existing
    else:
        raise HTTPException(
            status_code=404,
            detail="Author not found."
        )
    
def list_authors_service():
    authors = get_all_authors()
    if not authors:
        raise HTTPException(
            status_code=404,
            detail="No authors found."
        )
    return authors