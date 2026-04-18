from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Reader
from schemas import ReaderCreate, ReaderOut, ReaderUpdate

router = APIRouter(prefix="/readers", tags=["readers"])


@router.get("/", response_model=list[ReaderOut])
def list_readers(db: Session = Depends(get_db)):
    return db.execute(select(Reader)).scalars().all()


@router.post("/", response_model=ReaderOut, status_code=status.HTTP_201_CREATED)
def create_reader(data: ReaderCreate, db: Session = Depends(get_db)):
    existing = db.execute(select(Reader).where(Reader.email == data.email)).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")
    reader = Reader(**data.model_dump())
    db.add(reader)
    db.commit()
    db.refresh(reader)
    return reader


@router.get("/{reader_id}", response_model=ReaderOut)
def get_reader(reader_id: int, db: Session = Depends(get_db)):
    reader = db.get(Reader, reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return reader


@router.patch("/{reader_id}", response_model=ReaderOut)
def update_reader(reader_id: int, data: ReaderUpdate, db: Session = Depends(get_db)):
    reader = db.get(Reader, reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    updates = data.model_dump(exclude_unset=True)
    if "email" in updates:
        conflict = db.execute(
            select(Reader).where(Reader.email == updates["email"], Reader.id != reader_id)
        ).scalar_one_or_none()
        if conflict:
            raise HTTPException(status_code=409, detail="Email already registered")
    for field, value in updates.items():
        setattr(reader, field, value)
    db.commit()
    db.refresh(reader)
    return reader


@router.delete("/{reader_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reader(reader_id: int, db: Session = Depends(get_db)):
    reader = db.get(Reader, reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    db.delete(reader)
    db.commit()
