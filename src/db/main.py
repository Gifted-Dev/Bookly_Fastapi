from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config 
from src.books.Books_model import Book

async_engine = AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True
))

# # Use create_async_engine for asynchronous support
# async_engine = create_async_engine(
#     url=Config.DATABASE_URL,
#     echo=True
# )

async def init_db():
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        print("Database initialization successful")
    except Exception as e:
        print(f"Error initializing database: {e}")

async def get_session() -> AsyncSession:
    """Dependency to provide the session object"""
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    
    async with async_session() as session:
        yield session