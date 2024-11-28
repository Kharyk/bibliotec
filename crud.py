from sqlalchemy.orm import Session
from derectoria.models import Author, Book
#import derectoria.schemas

def get_author(db, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_authors(db, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

"""def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author"""

def get_book(db, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db, skip: int = 0, limit: int = 10):
    return 123 #db.query(Book).offset(skip).limit(limit).all()


"""
def create_book(db, book: schemas.BookCreate):
    db_book = models.Book(
        name=book.name,
        genre=book.genre,
        author_id=book.author_id,
        year=book.year,
        pages=book.pages
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
    
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return None
    db_book.name = book.name
    db_book.genre = book.genre
    db_book.author_id = book.author_id
    db_book.year = book.year
    db_book.pages = book.pages
    db.commit()
    db.refresh(db_book)
    return db_book
"'' '΅"' '' ""
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book


""" 







"""
from sqlalchemy.orm import Session
from derectoria import models, schemas


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_data: schemas.BookCreate):
    db.query(models.Book).filter(models.Book.id == book_id).update(book_data.dict())
    db.commit()
    return get_book_by_id(db, book_id)

def delete_book(db: Session, book_id: int):
    db.query(models.Book).filter(models.Book.id == book_id).delete()
    db.commit()
    return {"message": "Book deleted successfully"}



def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()

def get_author_by_id(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def update_author(db: Session, author_id: int, author_data: schemas.AuthorCreate):
    db.query(models.Author).filter(models.Author.id == author_id).update(author_data.dict())
    db.commit()
    return get_author_by_id(db, author_id)

def delete_author(db: Session, author_id: int):
    db.query(models.Author).filter(models.Author.id == author_id).delete()
    db.commit()
    return {"message": "Author deleted successfully"} """
