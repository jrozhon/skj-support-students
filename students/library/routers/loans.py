from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Copy, Loan, LoanStatus, Reader
from schemas import LoanCreate, LoanDetailOut, LoanOut, LoanReturn

router = APIRouter(prefix="/loans", tags=["loans"])


@router.get("/", response_model=list[LoanDetailOut])
def list_loans(
    status: LoanStatus | None = None,
    reader_id: int | None = None,
    db: Session = Depends(get_db),
):
    stmt = select(Loan)
    if status is not None:
        stmt = stmt.where(Loan.status == status)
    if reader_id is not None:
        stmt = stmt.where(Loan.reader_id == reader_id)
    return db.execute(stmt).scalars().all()


@router.post("/", response_model=LoanOut, status_code=status.HTTP_201_CREATED)
def create_loan(data: LoanCreate, db: Session = Depends(get_db)):
    reader = db.get(Reader, data.reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")

    copy = db.get(Copy, data.copy_id)
    if not copy:
        raise HTTPException(status_code=404, detail="Copy not found")

    if not copy.available:
        raise HTTPException(status_code=409, detail="Copy is already loaned out")

    loan = Loan(
        reader_id=data.reader_id,
        copy_id=data.copy_id,
        loan_date=data.loan_date,
        due_date=data.due_date,
        status=LoanStatus.active,
    )
    copy.available = False
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan


@router.get("/{loan_id}", response_model=LoanDetailOut)
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.get(Loan, loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


@router.post("/{loan_id}/return", response_model=LoanOut)
def return_loan(loan_id: int, data: LoanReturn, db: Session = Depends(get_db)):
    loan = db.get(Loan, loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    if loan.status == LoanStatus.returned:
        raise HTTPException(status_code=409, detail="Loan has already been returned")

    if data.return_date < loan.loan_date:
        raise HTTPException(status_code=422, detail="return_date cannot be before loan_date")

    loan.return_date = data.return_date
    loan.status = LoanStatus.returned
    loan.copy.available = True
    db.commit()
    db.refresh(loan)
    return loan


@router.get("/reader/{reader_id}/active", response_model=list[LoanDetailOut])
def active_loans_for_reader(reader_id: int, db: Session = Depends(get_db)):
    reader = db.get(Reader, reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    stmt = select(Loan).where(Loan.reader_id == reader_id, Loan.status == LoanStatus.active)
    return db.execute(stmt).scalars().all()
