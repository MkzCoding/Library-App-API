from pydantic import BaseModel
class BookOut(BaseModel):
    id: int
    title: str
    author_id: int
    isbn: str
    available: bool = True
    
    class Config:
        orm_mode = True

class BookCreatedOut(BaseModel):
    success: bool
    book_id: int

    class Config:
        orm_mode = True

