from fastapi import Request, HTTPException

def require_librarian_admin(request: Request):
    if request.state.user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    
def require_librarian_employee(request: Request):
    if request.state.user["role"] != "employee":
        raise HTTPException(status_code=403, detail="Forbidden.")