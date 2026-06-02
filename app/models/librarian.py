from pydantic import BaseModel

class Librarian(BaseModel):
    id: int
    name: str
    email: str
    role: str
    username: str
    hashed_password: str