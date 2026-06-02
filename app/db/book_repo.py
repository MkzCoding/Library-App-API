from app.db.init_db import get_connection
from app.models.book import Book
def add_book(title, author_id, isbn, available=True):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author_id, isbn, available) VALUES (?, ?, ?, ?)",
         (title, author_id, isbn, available) 
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, author_id, isbn, available FROM books WHERE available = 1"
    )
    rows = cursor.fetchall()
    conn.close()
    return [Book(**dict(row)) for row in rows] 

def get_book_by_id(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE id = ?", (book_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return Book(**dict(row)) if row else None

def get_book_by_isbn(book_isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE isbn = ?",(book_isbn,)
    )
    row = cursor.fetchone()
    conn.close()
    return Book(**dict(row)) if row else None

def update_book_availability(book_id, available):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET available = ? WHERE id = ?", (available, book_id)
    )
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM books WHERE id = ?", (book_id,)
    )
    deleted_book = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_book