from pydantic import BaseModel

class AuthorCreated(BaseModel):
    success: bool
    author_id: int
    
    class Config:
        orm_mode = True

class AuthorOut(BaseModel):
    id: int
    name: str
    nationality: str

    class Config:
        orm_mode = True