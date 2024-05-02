import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from typing import Dict, List, Annotated
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from fastapi import Query





app = FastAPI(title="Read your favorite Book ")
books = []

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
 
@app.get("/")
def index(request: Request):
    for book in books:
        book["genres_with_index"] = [(index, genre) for index, genre in enumerate(book["genre"])]
    return templates.TemplateResponse("index.html", {"request": request, "books": books})

@app.get("/search")
def search_books(query: str):
    return [book for book in books if query.lower() in book['name'].lower()]
    

@app.post("/add_book")
def add_book(name: str, author: str, genre: str, year: int, pages: int):
    genres = [g.strip() for g in genre.split(",")]  
    books.append({
        "name": name,
        "genre": genres,
        "author": author,
        "year": year,
        "pages": pages
    })
    return {"msg": "Book was added"}


@app.get("/get_name_of_book")
def get_name_of_book():
    return books


@app.get("/books/by_author/")
async def get_books_by_author(author: str = Query(...)):
    filtered_books = [book for book in books if book.author == author]
    return filtered_books


@app.get("/books/by_genre/")
async def get_books_by_genre(genre: str = Query(...)):
    filtered_books = [book for book in books if book.genre == genre]
    return filtered_books


@app.delete("/remove/{name}")
def delete_book(name: str):
    for book in books:
        if book['name'] == name:
            books.remove(book)
            return "Книга була видалений"
    return "Книга не була знайдений"


if __name__ ==  "__main__":
    uvicorn.run(app, port=8804)
