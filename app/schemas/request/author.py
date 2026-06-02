from pydantic import BaseModel

class AddAuthor(BaseModel):
    name:str
    nationality:str