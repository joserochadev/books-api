from unittest.mock import MagicMock

from django.test import TestCase

from books.repositories.IBookRepository import IBookRepository
from books.useCases.ListBooksUseCase import ListBooksUseCase


class TestListBooksUseCase(TestCase):
    def setUp(self):
        self.mock_repository = MagicMock(IBookRepository)

        self.sut = ListBooksUseCase(self.mock_repository)

    def test_it_should_be_able_to_list_all_books(self):
        self.mock_repository.listBooks.return_value = [
            {
                "id": 1,
                "title": "O Senhor dos Anéis",
                "author": "J.R.R. Tolkien",
                "release_year": 1954,
                "isbn": "978-0-261-10325-7"
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "release_year": 1949,
                "isbn": "978-0-452-28423-4"
            }
        ]

        books = self.sut.execute()

        self.assertEqual(len(books), 2)
        self.assertEqual(books[0]['title'], "O Senhor dos Anéis")

    def test_it_should_raise_an_exception_when_book_list_is_empty(self):
        self.mock_repository.listBooks.return_value = []

        with self.assertRaises(Exception) as context:
            self.sut.execute()

        self.assertEqual(str(context.exception), "Books list is empty")
