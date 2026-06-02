from pydantic import BaseModel

class Book(BaseModel):
    id: int | None = None
    title: str
    author_id: int
    available: bool = True
    isbn: str