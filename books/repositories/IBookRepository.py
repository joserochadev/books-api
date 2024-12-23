from abc import ABC, abstractmethod

from pydantic import BaseModel

from books.models import Book


class ICreateBookSchema(BaseModel):
    title: str
    author: str
    release_year: int
    isbn: str


class IBookRepository(ABC):
    @abstractmethod
    def create_book(self, data: ICreateBookSchema) -> Book:
        """ Método usado pra criar um livro """
        pass

    @abstractmethod
    def get_book_by_isbn(self, isbn: str) -> Book | None:
        pass

    @abstractmethod
    def get_book_by_id(self, id: str) -> Book | None:
        pass

    @abstractmethod
    def listBooks(self) -> list[Book]:
        pass

    @abstractmethod
    def remove_book(self, id: str):
        pass
