from datetime import date
from pydantic import BaseModel, EmailStr, model_validator
from models import CopyCondition, LoanStatus


# --- Author ---

class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_year: int | None = None


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    birth_year: int | None = None


class AuthorOut(AuthorBase):
    id: int

    model_config = {"from_attributes": True}


# --- Book ---

class BookBase(BaseModel):
    title: str
    isbn: str | None = None
    published_year: int | None = None
    author_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    isbn: str | None = None
    published_year: int | None = None
    author_id: int | None = None


class BookOut(BookBase):
    id: int
    author: AuthorOut

    model_config = {"from_attributes": True}


class BookAvailability(BaseModel):
    book_id: int
    title: str
    total_copies: int
    available_copies: int

    model_config = {"from_attributes": True}


# --- Copy ---

class CopyBase(BaseModel):
    book_id: int
    condition: CopyCondition = CopyCondition.good


class CopyCreate(CopyBase):
    pass


class CopyUpdate(BaseModel):
    condition: CopyCondition | None = None
    available: bool | None = None


class CopyOut(CopyBase):
    id: int
    available: bool

    model_config = {"from_attributes": True}


# --- Reader ---

class ReaderBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    registered_at: date


class ReaderCreate(ReaderBase):
    pass


class ReaderUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None


class ReaderOut(ReaderBase):
    id: int

    model_config = {"from_attributes": True}


# --- Loan ---

class LoanCreate(BaseModel):
    reader_id: int
    copy_id: int
    loan_date: date
    due_date: date

    @model_validator(mode="after")
    def due_after_loan(self) -> "LoanCreate":
        if self.due_date <= self.loan_date:
            raise ValueError("due_date must be after loan_date")
        return self


class LoanReturn(BaseModel):
    return_date: date


class LoanOut(BaseModel):
    id: int
    reader_id: int
    copy_id: int
    loan_date: date
    due_date: date
    return_date: date | None
    status: LoanStatus

    model_config = {"from_attributes": True}


class LoanDetailOut(BaseModel):
    id: int
    reader_id: int
    copy_id: int
    loan_date: date
    due_date: date
    return_date: date | None
    status: LoanStatus
    reader: ReaderOut
    copy: CopyOut

    model_config = {"from_attributes": True, "warnings": False}
