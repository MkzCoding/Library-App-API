from fastapi import APIRouter, Depends
from app.services.book_service import add_book_service, get_book_by_isbn_service,list_available_books_service, remove_book_service,update_book_availability_service
from app.schemas.request.book import BookCreate, BookAvailabilityUpdate
from app.schemas.response.book import BookOut, BookCreatedOut
from app.middleware.dependencies import require_librarian_admin, require_librarian_employee
router = APIRouter()

@router.get("/books", response_model=list[BookOut])
def get_all_books():
    books = list_available_books_service()
    return books
@router.post("/books", response_model=BookCreatedOut, dependencies=[Depends(require_librarian_employee)])
def add_book(book: BookCreate):
    new_id = add_book_service(book.title, book.author_id, book.isbn)
    return new_id
@router.get("/books/{book_isbn}")
def get_book_by_isbn(book_isbn):
    book = get_book_by_isbn_service(book_isbn)
    return book
@router.put("/books/{book_isbn}", dependencies=[Depends(require_librarian_employee)])
def update_book_availability(book_isbn:str, update: BookAvailabilityUpdate):
    result = update_book_availability_service(book_isbn, update.available)
    return result
@router.delete("/books/{book_id}", dependencies=[Depends(require_librarian_employee)])
def delete_book(book_id):
    result = remove_book_service(book_id)
    return result