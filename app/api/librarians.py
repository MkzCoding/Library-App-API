from fastapi import APIRouter, Depends
from app.services.librarian_service import add_librarian_service,list_librarians_service,get_librarian_by_id_service,update_librarian_email_service,update_librarian_role_service, remove_librarian_service
from app.schemas.request.librarian import CreateLibrarian, LibrarianEmailUpdate, LibrarianRoleUpdate
from app.schemas.response.librarian import LibrarianOut, CreatedLibrarian, LibrarianEmailUpdateResponse, LibrarianRoleUpdateResponse, LibrarianRemovedResponse
from app.middleware.dependencies import require_librarian_admin
router = APIRouter()

@router.get("/librarians", response_model= list[LibrarianOut], dependencies=[Depends(require_librarian_admin)])
def get_all_librarians():
    librarians = list_librarians_service()
    return librarians
@router.post("/librarians", response_model= CreatedLibrarian, dependencies=[Depends(require_librarian_admin)])
def add_librarian(librarian: CreateLibrarian):
    new_id = add_librarian_service(librarian.name, librarian.email, librarian.role, librarian.username, librarian.password)
    return new_id
@router.get("/librarians/{id}", response_model= LibrarianOut, dependencies=[Depends(require_librarian_admin)])
def get_librarian_by_id(id):
    librarian = get_librarian_by_id_service(id)
    return librarian
@router.put("/librarians/{id}/email", response_model = LibrarianEmailUpdateResponse, dependencies=[Depends(require_librarian_admin)])
def update_librarian_email(id:int, librarian: LibrarianEmailUpdate):
    result = update_librarian_email_service(id, librarian.email)
    return result
@router.put("/librarians/{id}/role", response_model= LibrarianRoleUpdateResponse, dependencies=[Depends(require_librarian_admin)])
def update_librarian_role(id:int, librarian: LibrarianRoleUpdate):
    result = update_librarian_role_service(id, librarian.role)
    return result
@router.delete("/librarians/{id}", response_model= LibrarianRemovedResponse, dependencies=[Depends(require_librarian_admin)])
def remove_librarian(id):
    result = remove_librarian_service(id)
    return result