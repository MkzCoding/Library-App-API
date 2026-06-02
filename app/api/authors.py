from fastapi import APIRouter, Depends
from app.services.author_service import add_author_service, remove_author_service, get_author_by_id_service, list_authors_service
from app.schemas.request.author import AddAuthor
from app.schemas.response.author import AuthorCreated, AuthorOut
from app.middleware.dependencies import require_librarian_admin, require_librarian_employee
router = APIRouter()

@router.post("/authors", response_model = AuthorCreated, dependencies=[Depends(require_librarian_admin)])
def add_author(author: AddAuthor):
    new_id = add_author_service(author.name, author.nationality)
    return new_id
@router.get("/authors", response_model = list[AuthorOut], dependencies=[Depends(require_librarian_employee)])
def get_all_authors():
    authors = list_authors_service()
    return authors
@router.get("/authors/{id}", response_model= AuthorOut, dependencies=[Depends(require_librarian_employee)])
def get_author_by_id(id: int):
    author = get_author_by_id_service(id)
    return author
@router.delete("/authors/{id}", dependencies=[Depends(require_librarian_admin)])
def remove_author(id: int):
    result = remove_author_service(id)
    return result