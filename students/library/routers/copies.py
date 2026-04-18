from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Book, Copy
from schemas import CopyCreate, CopyOut, CopyUpdate

router = APIRouter(prefix="/copies", tags=["copies"])


@router.get("/", response_model=list[CopyOut])
def list_copies(book_id: int | None = None, available: bool | None = None, db: Session = Depends(get_db)):
    stmt = select(Copy)
    if book_id is not None:
        stmt = stmt.where(Copy.book_id == book_id)
    if available is not None:
        stmt = stmt.where(Copy.available == available)
    return db.execute(stmt).scalars().all()


@router.post("/", response_model=CopyOut, status_code=status.HTTP_201_CREATED)
def create_copy(data: CopyCreate, db: Session = Depends(get_db)):
    if not db.get(Book, data.book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    copy = Copy(**data.model_dump())
    db.add(copy)
    db.commit()
    db.refresh(copy)
    return copy


@router.get("/{copy_id}", response_model=CopyOut)
def get_copy(copy_id: int, db: Session = Depends(get_db)):
    copy = db.get(Copy, copy_id)
    if not copy:
        raise HTTPException(status_code=404, detail="Copy not found")
    return copy


@router.patch("/{copy_id}", response_model=CopyOut)
def update_copy(copy_id: int, data: CopyUpdate, db: Session = Depends(get_db)):
    copy = db.get(Copy, copy_id)
    if not copy:
        raise HTTPException(status_code=404, detail="Copy not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(copy, field, value)
    db.commit()
    db.refresh(copy)
    return copy


@router.delete("/{copy_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_copy(copy_id: int, db: Session = Depends(get_db)):
    copy = db.get(Copy, copy_id)
    if not copy:
        raise HTTPException(status_code=404, detail="Copy not found")
    db.delete(copy)
    db.commit()
