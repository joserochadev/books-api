from django.test import TestCase

from books.repositories.booksRepositories.BookRepository import BookRepository
from books.useCases.CreateBookUseCase import (CreateBookUseCase,
                                              _ICreateBookUseCaseRequest)


class TestCreateBookUseCase(TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.current_book = {
            "title": "O Símbolo Perdido",
            "author": "Dan Brown",
            "release_year": 2009,
            "isbn": "0-552-15176-4"
        }
        self.repository = BookRepository()
        self.sut = CreateBookUseCase(repository=self.repository)
        self.request_data = _ICreateBookUseCaseRequest(**self.current_book)

    def test_it_should_be_able_to_create_a_book(self):
        book = self.sut.execute(self.request_data)

        # assert book.title == "O Símbolo Perdido"
        self.assertEqual(book.title, "O Símbolo Perdido")

    def test_it_should_not_be_able_to_create_two_books_with_same_isbn(self):
        self.sut.execute(self.request_data)

        with self.assertRaises(Exception):
            self.sut.execute(self.request_data)
