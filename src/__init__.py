from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print("Server is starting ...")
    try:
        await init_db()
        print("Database initialization completed.")
    except Exception as e:
        print(f"Error initializing database: {e}")
    yield    
    print("Server has been stopped ...")

version = 'v1'

app = FastAPI(
    title='Bookly',
    description="A REST API for a book review web service",
    version=version,
    lifespan=life_span
)


app.include_router(book_router, prefix="/api/{version}/books", tags=['books'])