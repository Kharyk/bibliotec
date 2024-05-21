import uvicorn
from fastapi import FastAPI, Depends, Query, HTTPException, status
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from typing import List
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
from derectoria import crud_1, crud
from derectoria import database
from derectoria import models 
from derectoria import schemas
from fastapi.security import HTTPBasic, HTTPBasicCredentials

import secrets



app = FastAPI(title="Read your favorite Book ")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

security = HTTPBasic()


def check_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "secret")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def get_db():
    db = database.Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index(request: Request, db = Depends(get_db), username = Depends(check_credentials)):
    books = crud_1.get_books(db)
    return templates.TemplateResponse("index.html", {"request": request, "books": books})
    return {"message": f"Hello, {username}! You are authorized."}



@app.get("/search")
def search_books(query: str, db = Depends(get_db), username = Depends(check_credentials)):
    return crud.search_books(db, query)


@app.post("/add_book")
def add_book(name: str, author: str, genre: str, year: int, pages: int, db = Depends(get_db), username = Depends(check_credentials)):
    return crud.create_book(db, name, author, genre, year, pages)

@app.get("/get_name_of_book")
def get_name_of_book(db  = Depends(get_db), username = Depends(check_credentials)):
    return crud.get_name_of_book(db)


@app.get("/books/by_author/")
def get_books_by_author(author: str = Query(...), db = Depends(get_db), username = Depends(check_credentials)):
    return crud.get_books_by_author(db, author)


@app.get("/books/by_genre/")
def get_books_by_genre(genre: str = Query(...), db = Depends(get_db), username = Depends(check_credentials)):
    return crud.get_books_by_genre(db, genre)


@app.delete("/remove/{name}")
def delete_book(name: str, db  = Depends(get_db), username = Depends(check_credentials)):
    return crud.delete_book(db, name)


if __name__ == "__main__":
    uvicorn.run(app, port=8808)
