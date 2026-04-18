from fastapi import FastAPI

from database import Base, engine
from routers import authors, books, copies, loans, readers

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API")

app.include_router(authors.router)
app.include_router(books.router)
app.include_router(copies.router)
app.include_router(readers.router)
app.include_router(loans.router)
