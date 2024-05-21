from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from derectoria import database 
from derectoria.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author")
    genre = Column(String)
    year = Column(Integer)
    pages = Column(Integer)

    
    """ from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from derectoria.database import Base

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    pages = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")


class User(Base):
    __tablename__ =  "user"
    id = Column(Integer, primary_key = True, index = True)
    
    name = Column(String, index = True)
    password = Column(Integer) """