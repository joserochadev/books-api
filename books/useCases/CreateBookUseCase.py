from pydantic import BaseModel

from books.models import Book

from ..repositories.IBookRepository import IBookRepository


class _ICreateBookUseCaseRequest(BaseModel):
    title: str
    author: str
    release_year: int
    isbn: str


class CreateBookUseCase:
    def __init__(self, repository: IBookRepository) -> Book:
        self.repository = repository

    def execute(self, data: _ICreateBookUseCaseRequest):
        book_already_exists = self.repository.get_book_by_isbn(data.isbn)

        if (book_already_exists):
            raise Exception('ERRO: Book already exists.')

        book = self.repository.create_book(data)
        return book
        # print(book)
        # print(data)
