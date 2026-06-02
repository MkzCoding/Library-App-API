from pydantic import BaseModel

class LibrarianOut(BaseModel):
    username: str
    role: str

    class Config:
       orm_mode = True

class CreatedLibrarian(BaseModel):
    username : str
    message: str
    role: str

    class Config:
        orm_mode = True

class LibrarianEmailUpdateResponse(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True

class LibrarianRoleUpdateResponse(BaseModel):
    success: bool
    message: str
    
    class config:
        orm_mode = True


class LibrarianRemovedResponse(BaseModel):
    success: bool
    message: str

    class config:
        orm_mode = True