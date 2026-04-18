from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from database import get_db
from models import Author, Book, Copy
from schemas import BookAvailability, BookCreate, BookOut, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookOut])
def list_books(author_id: int | None = None, db: Session = Depends(get_db)):
    stmt = select(Book)
    if author_id is not None:
        stmt = stmt.where(Book.author_id == author_id)
    return db.execute(stmt).scalars().all()


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    if not db.get(Author, data.author_id):
        raise HTTPException(status_code=404, detail="Author not found")
    book = Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.patch("/{book_id}", response_model=BookOut)
def update_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    updates = data.model_dump(exclude_unset=True)
    if "author_id" in updates and not db.get(Author, updates["author_id"]):
        raise HTTPException(status_code=404, detail="Author not found")
    for field, value in updates.items():
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()


@router.get("/{book_id}/availability", response_model=BookAvailability)
def book_availability(book_id: int, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    total = db.execute(
        select(func.count()).select_from(Copy).where(Copy.book_id == book_id)
    ).scalar_one()
    available = db.execute(
        select(func.count()).select_from(Copy).where(Copy.book_id == book_id, Copy.available == True)
    ).scalar_one()
    return BookAvailability(
        book_id=book.id,
        title=book.title,
        total_copies=total,
        available_copies=available,
    )
