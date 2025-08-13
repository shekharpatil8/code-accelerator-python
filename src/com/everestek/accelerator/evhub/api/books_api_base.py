# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from com.everestek.accelerator.evhub.dto.book import Book
from com.everestek.accelerator.evhub.dto.error import Error


class BaseBooksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBooksApi.subclasses = BaseBooksApi.subclasses + (cls,)
    async def create_book(
        self,
        book: Book,
    ) -> None:
        """Adds a new book to the collection with details such as title, author, and published year."""
        ...


    async def get_book_by_id(
        self,
        bookId: str,
    ) -> Book:
        """Retrieves details of a single book by its unique identifier."""
        ...


    async def list_books(
        self,
        limit: int,
    ) -> List[Book]:
        """Retrieves a paginated list of books from the collection."""
        ...
