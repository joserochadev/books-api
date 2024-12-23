from books.models import Book
from books.repositories.IBookRepository import IBookRepository


class GetBookUseCase:
    def __init__(self, repository: IBookRepository):
        self.repository = repository

    def execute(self, book_id: str) -> Book:
        book = self.repository.get_book_by_id(book_id)

        if not book:
            raise Exception("Book not found.")

        return book
