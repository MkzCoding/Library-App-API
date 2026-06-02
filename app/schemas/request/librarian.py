from pydantic import BaseModel

class CreateLibrarian(BaseModel):
    name: str
    email: str
    role: str
    username: str
    password: str

class LibrarianEmailUpdate(BaseModel):
    email:str

class LibrarianRoleUpdate(BaseModel):
    role:str