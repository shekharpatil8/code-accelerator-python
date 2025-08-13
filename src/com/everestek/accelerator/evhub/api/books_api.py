# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from com.everestek.accelerator.evhub.api.books_api_base import BaseBooksApi
import com.everestek.accelerator.evhub.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from com.everestek.accelerator.evhub.dto.extra_models import TokenModel  # noqa: F401
from com.everestek.accelerator.evhub.dto.book import Book
from com.everestek.accelerator.evhub.dto.error import Error


router = APIRouter()

ns_pkg = com.everestek.accelerator.evhub.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/books",
    responses={
        201: {"description": "Book created successfully"},
        200: {"model": Error, "description": "Unexpected error"},
    },
    tags=["books"],
    summary="Create a new book",
    response_model_by_alias=True,
)
async def create_book(
    book: Book = Body(None, description="JSON object containing the details of the book to be created."),
) -> None:
    """Adds a new book to the collection with details such as title, author, and published year."""
    if not BaseBooksApi.subclasses:
        raise HTTPException(status_code=501, detail="Not implemented")

    if len(BaseBooksApi.subclasses) > 1:
        raise HTTPException(status_code=500, detail="Multiple implementations found, You can have only one implementation for the base class")
            
    return await BaseBooksApi.subclasses[0]().create_book(book)


@router.get(
    "/books/{bookId}",
    responses={
        200: {"model": Book, "description": "Information for the requested book"},
        200: {"model": Error, "description": "Unexpected error"},
    },
    tags=["books"],
    summary="Get information about a specific book",
    response_model_by_alias=True,
)
async def get_book_by_id(
    bookId: str = Path(..., description="The ID of the book to retrieve"),
) -> Book:
    """Retrieves details of a single book by its unique identifier."""
    if not BaseBooksApi.subclasses:
        raise HTTPException(status_code=501, detail="Not implemented")

    if len(BaseBooksApi.subclasses) > 1:
        raise HTTPException(status_code=500, detail="Multiple implementations found, You can have only one implementation for the base class")
            
    return await BaseBooksApi.subclasses[0]().get_book_by_id(bookId)


@router.get(
    "/books",
    responses={
        200: {"model": List[Book], "description": "A paged array of books"},
        200: {"model": Error, "description": "Unexpected error"},
    },
    tags=["books"],
    summary="List all books",
    response_model_by_alias=True,
)
async def list_books(
    limit: int = Query(None, description="How many books to return at one time (max 50)", alias="limit", le=50),
) -> List[Book]:
    """Retrieves a paginated list of books from the collection."""
    if not BaseBooksApi.subclasses:
        raise HTTPException(status_code=501, detail="Not implemented")

    if len(BaseBooksApi.subclasses) > 1:
        raise HTTPException(status_code=500, detail="Multiple implementations found, You can have only one implementation for the base class")
            
    return await BaseBooksApi.subclasses[0]().list_books(limit)
