from app.db.init_db import get_connection
from app.schemas.response.member import MemberOut
def add_member(member_name, member_email, member_membership_date, member_username, member_hashed_password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO members (name, email, membership_date, username, hashed_password) VALUES (?, ?, ?, ?, ?)", 
        (member_name, member_email, member_membership_date, member_username, member_hashed_password)
    )
    conn.commit()
    conn.close()

def get_member_by_id(member_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, membership_date, loan_count FROM members WHERE id = ?", (member_id,)
    )
    row = cursor.fetchone()
    conn.close()
    member = MemberOut(**dict(row)) if row else None
    return member

def get_member_by_username(member_username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, hashed_password FROM members WHERE username = ?", (member_username,)
    )
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_members():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, membership_date, loan_count FROM members"
    )
    rows = cursor.fetchall()
    conn.close()
    return [MemberOut(**dict(row)) for row in rows]

def update_member_email(member_id, member_email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE members SET email = ? WHERE id = ?",(member_email, member_id)
    )
    conn.commit()
    conn.close()

def update_member_membership(member_id, member_membership_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE members SET membership_date = ? WHERE id = ?",(member_membership_date, member_id)
    )
    conn.commit()
    conn.close()

def update_member_loan_count(member_id, member_loan_count):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE members SET loan_count = ? WHERE id = ?", (member_loan_count, member_id)
    )
    conn.commit()
    conn.close()

def delete_member(member_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM members WHERE id = ?",(member_id,)
    )
    deleted_row = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_row
