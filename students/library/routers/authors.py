from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Author
from schemas import AuthorCreate, AuthorOut, AuthorUpdate

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/", response_model=list[AuthorOut])
def list_authors(db: Session = Depends(get_db)):
    return db.execute(select(Author)).scalars().all()


@router.post("/", response_model=AuthorOut, status_code=status.HTTP_201_CREATED)
def create_author(data: AuthorCreate, db: Session = Depends(get_db)):
    author = Author(**data.model_dump())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@router.get("/{author_id}", response_model=AuthorOut)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.patch("/{author_id}", response_model=AuthorOut)
def update_author(author_id: int, data: AuthorUpdate, db: Session = Depends(get_db)):
    author = db.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(author, field, value)
    db.commit()
    db.refresh(author)
    return author


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
