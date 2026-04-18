from datetime import date
from sqlalchemy import ForeignKey, String, Date, Boolean, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from database import Base


class LoanStatus(str, enum.Enum):
    active = "active"
    returned = "returned"


class CopyCondition(str, enum.Enum):
    good = "good"
    damaged = "damaged"
    lost = "lost"


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    birth_year: Mapped[int | None] = mapped_column(nullable=True)

    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[str | None] = mapped_column(String(20), nullable=True, unique=True)
    published_year: Mapped[int | None] = mapped_column(nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship("Author", back_populates="books")
    copies: Mapped[list["Copy"]] = relationship("Copy", back_populates="book")


class Copy(Base):
    __tablename__ = "copies"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    condition: Mapped[CopyCondition] = mapped_column(
        SAEnum(CopyCondition), default=CopyCondition.good
    )
    available: Mapped[bool] = mapped_column(Boolean, default=True)

    book: Mapped["Book"] = relationship("Book", back_populates="copies")
    loans: Mapped[list["Loan"]] = relationship("Loan", back_populates="copy")


class Reader(Base):
    __tablename__ = "readers"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    registered_at: Mapped[date] = mapped_column(Date)

    loans: Mapped[list["Loan"]] = relationship("Loan", back_populates="reader")


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"))
    copy_id: Mapped[int] = mapped_column(ForeignKey("copies.id"))
    loan_date: Mapped[date] = mapped_column(Date)
    due_date: Mapped[date] = mapped_column(Date)
    return_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    status: Mapped[LoanStatus] = mapped_column(
        SAEnum(LoanStatus), default=LoanStatus.active
    )

    reader: Mapped["Reader"] = relationship("Reader", back_populates="loans")
    copy: Mapped["Copy"] = relationship("Copy", back_populates="loans")
