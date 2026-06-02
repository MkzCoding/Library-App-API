from fastapi import HTTPException
from app.db.book_repo import add_book, get_book_by_isbn, delete_book, get_all_books, update_book_availability
from app.db.loan_repo import get_active_loans

def add_book_service(title, author_id, book_isbn):
    existing = get_book_by_isbn(book_isbn)
    if existing:
        raise HTTPException(
            status_code=409,
            detail="Book already exists."
        )
    new_id = add_book(title,author_id,book_isbn)
    return {"success":True, "book_id":new_id}

def remove_book_service(book_id):
    loans = get_active_loans()
    for loan in loans:
        if book_id == loan["book_id"]:
            raise HTTPException(
                status_code=409,
                detail="Book is currently loaned."
            )
    rows_deleted = delete_book(book_id)
    return {"success":rows_deleted > 0, "message":"Book Deleted" if rows_deleted else "Book not found."}

def get_book_by_isbn_service(book_isbn):
    existing = get_book_by_isbn(book_isbn)
    if existing:
        return existing
    else:
        raise HTTPException(
            status_code=404,
            detail="Book not found."
        )
    
def list_available_books_service():
    books = get_all_books()
    if not books:
        raise HTTPException(
            status_code=404,
            detail="No books found."
        )
    for book in books:
        book.available = True
    return [book for book in books if book.available == True]


def update_book_availability_service(book_isbn, available):
    existing = get_book_by_isbn(book_isbn)
    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Book not found."
        )
    if existing.available == available:
        raise HTTPException(
            status_code=409,
            detail=f"Book is already {'available' if available == 1 else 'unvailable'}."
        )
    else:
        book_id = existing.id
        update_book_availability(book_id, available)
        return {"success":True, "message":"Book availability updated."}