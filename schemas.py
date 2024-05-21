from pydantic import BaseModel
from typing import List

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    name: str
    genre: str
    author_id: int
    year: int
    pages: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author: Author

class Config:
    orm_mode = True

        
"""from pydantic import BaseModel
from typing import List
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(BaseModel):
    message: str


class BookBase(BaseModel):
    title: str
    year: int
    pages: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List[Book] = []

    class Config:
        orm_mode = True """
