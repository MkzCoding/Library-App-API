from app.db.init_db import get_connection
from app.schemas.response.librarian import LibrarianOut
def add_librarian(librarian_name, librarian_email, librarian_role, librarian_username, librarian_hashed_password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO librarians (name, email, role, username, hashed_password) VALUES (?, ?, ?, ?, ?)", 
            (librarian_name, librarian_email, librarian_role, librarian_username, librarian_hashed_password)
        
    )
    conn.commit()
    conn.close()

def get_librarian_by_id(librarian_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, role FROM librarians WHERE id = ?", (librarian_id,)
    )
    row = cursor.fetchone()
    conn.close()
    librarian = LibrarianOut(**dict(row)) if row else None
    return librarian

def get_librarian_by_username(librarian_username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, role, hashed_password FROM librarians WHERE username = ?", (librarian_username,)
    )
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_librarians():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, role FROM librarians"
    )
    rows = cursor.fetchall()
    conn.close()
    return [LibrarianOut(**dict(row)) for row in rows]

def update_librarian_email(librarian_id, librarian_email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE librarians SET email = ? WHERE id = ?", (librarian_email, librarian_id)
    )
    conn.commit
    conn.close()

def update_librarian_role(librarian_id, librarian_role):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE librarians SET role = ? WHERE id = ?", (librarian_role, librarian_id)
    )
    conn.commit()
    conn.close()

def delete_librarian(librarian_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM librarians WHERE id = ?", (librarian_id,)
    )
    deleted_row = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_row