from app.db.init_db import get_connection
from app.models.loan import Loan
def add_loan(book_id, member_id, loan_date, return_date=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
      "INSERT INTO loans (book_id, member_id, loan_date, return_date) VALUES (?, ?, ?, ?)",
      (book_id, member_id, loan_date, return_date)
          )
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return new_id

def return_loan(loan_id, return_date):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute(
          "UPDATE loans SET return_date = ? WHERE id = ?", (return_date, loan_id)
     )
     conn.commit()
     conn.close()

def get_loan_by_id(loan_id):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute(
          "SELECT * FROM loans WHERE id = ?",(loan_id,)
     )
     row = cursor.fetchone()
     conn.close()
     loan = Loan(**dict(row)) if row else None
     return loan

def get_loans_by_member(member_id):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute(
          "SELECT * FROM loans WHERE member_id = ?",(member_id,)
     )
     rows = cursor.fetchall()
     conn.close()
     return [Loan(**dict(row)) for row in rows]

def get_active_loans():
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute(
          "SELECT * FROM loans WHERE return_date IS NULL"
     )
     rows = cursor.fetchall()
     conn.close()
     return [Loan(**dict(row)) for row in rows]
     

def get_all_loans():
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute(
          "SELECT * FROM loans"
     )
     rows = cursor.fetchall()
     conn.close()
     return [Loan(**dict(row)) for row in rows]

def delete_loan(loan_id):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute(
          "DELETE FROM loans WHERE id = ?",(loan_id,)
     )
     rows_deleted = cursor.rowcount
     conn.commit()
     conn.close()
     return rows_deleted