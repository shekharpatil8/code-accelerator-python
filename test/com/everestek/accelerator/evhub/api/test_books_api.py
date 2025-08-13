# coding: utf-8

from fastapi.testclient import TestClient


from com.everestek.accelerator.evhub.dto.book import Book  # noqa: F401
from com.everestek.accelerator.evhub.dto.error import Error  # noqa: F401


def test_create_book(client: TestClient):
    """Test case for create_book

    Create a new book
    """
    book = {"author":"author","id":"id","published_year":0,"title":"title"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/books",
    #    headers=headers,
    #    json=book,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_book_by_id(client: TestClient):
    """Test case for get_book_by_id

    Get information about a specific book
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/books/{bookId}".format(bookId='book_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_books(client: TestClient):
    """Test case for list_books

    List all books
    """
    params = [("limit", 56)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/books",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

