from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.books.schemas import BookCreateModel, BookUpdateModel, Book
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from typing import List

book_router = APIRouter()
book_service = BookService()


def raiseException():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')

@book_router.get('/', response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    book = await book_service.get_all_books(session)
    return book

@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book

@book_router.get('/{book_id}', response_model=Book)
async def get_book(book_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    book = book_service.get_book(book_id, session)
    
    if book:
        return book
    else:
        raiseException()

@book_router.patch("/{book_id}", response_model=Book)
async def update_book(book_id: str,book_update_data:BookUpdateModel, session: AsyncSession = Depends(get_session)) -> dict:
    updated_book = await book_service.update_book(book_id, book_update_data, session)
    
    if updated_book:
        return updated_book
    else:
        raiseException()


@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:str, session: AsyncSession = Depends(get_session)):
    book_to_delete = book_service.delete_book(book_id, session)
    
    if book_to_delete:
        return {}
    else:
        raiseException()
    
