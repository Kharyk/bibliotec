from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///example.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



"""from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker


engine = create_engine('sqlite:///example.db')
session_factory = sessionmaker(engine)
Base = declarative_base() 

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    genre TEXT
                  )''')
conn.commit()


class Book(BaseModel):
    title: str
    author: str
    genre: str


@app.post("/books/")
async def create_book(book: Book):
    cursor.execute('''INSERT INTO books (title, author, genre)
                      VALUES (?, ?, ?)''',
                   (book.title, book.author, book.genre))
    conn.commit()
    return {"message": "Book added successfully"}

@app.get("/books/")
async def get_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return {"books": books}

@app.get("/books/by_author/")
async def get_books_by_author(author: str = Query(...)):
    cursor.execute("SELECT * FROM books WHERE author=?", (author,))
    books = cursor.fetchall()
    return {"books": books}


@app.get("/books/by_genre/")
async def get_books_by_genre(genre: str = Query(...)):
    cursor.execute("SELECT * FROM books WHERE genre=?", (genre,))
    books = cursor.fetchall()
    return {"books": books} """
