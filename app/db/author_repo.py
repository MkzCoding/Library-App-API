from app.db.init_db import get_connection
from app.models.author import Author
def add_author(author_name, author_nationality):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO authors (name, nationality) VALUES (?, ?)", 
        (author_name, author_nationality)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_author_by_id(author_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM authors WHERE id = ?", (author_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return Author(**dict(row)) if row else None

def get_all_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, nationality FROM authors" 
    )
    rows = cursor.fetchall()
    conn.close()
    return [Author(**dict(row)) for row in rows]

def delete_author(author_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM authors WHERE id = ?", (author_id,)
    )
    conn.commit()
    deleted_row = cursor.rowcount
    conn.close()
    return deleted_row