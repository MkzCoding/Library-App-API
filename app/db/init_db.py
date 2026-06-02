import sqlite3

DB_NAME = "Library.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS books (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT NOT NULL,
         author_id INTEGER NOT NULL,
         isbn TEXT UNIQUE NOT NULL,
         available BOOLEAN NOT NULL DEFAULT 1
             );
    CREATE TABLE IF NOT EXISTS authors (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          nationality TEXT NOT NULL
             );
    CREATE TABLE IF NOT EXISTS librarians (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          email TEXT NOT NULL,
          role TEXT NOT NULL,
          username TEXT UNIQUE NOT NULL,
          hashed_password TEXT NOT NULL   
             );
    CREATE TABLE IF NOT EXISTS members (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          email TEXT NOT NULL,
          membership_date DATE NOT NULL, 
          loan_count INTEGER DEFAULT 0,
          username TEXT UNIQUE NOT NULL,
          hashed_password TEXT NOT NULL
             );
    CREATE TABLE IF NOT EXISTS loans (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          book_id INTEGER NOT NULL,
          member_id INTEGER NOT NULL,
          loan_date DATE NOT NULL,
          return_date DATE,    
          FOREIGN KEY(book_id) REFERENCES books(id),
          FOREIGN KEY(member_id) REFERENCES members(id)
             );
    
""");
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()