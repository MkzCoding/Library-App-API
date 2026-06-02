from pydantic import BaseModel

class BookCreate(BaseModel):
    title:str
    author_id:str
    isbn:str
class BookAvailabilityUpdate(BaseModel):
    available: int