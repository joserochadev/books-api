from unittest.mock import MagicMock

from django.test import TestCase

from books.repositories.IBookRepository import IBookRepository
from books.useCases.GetBookUseCase import GetBookUseCase


class TestGetBookUseCase(TestCase):

    def setUp(self):
        self.mock_repository = MagicMock(spec=IBookRepository)

        self.sut = GetBookUseCase(self.mock_repository)

    def mock_get_book_by_id(self, book_id):
        books = {
            '1': {
                "id": '1',
                "title": "O Senhor dos Anéis",
                "author": "J.R.R. Tolkien",
                "release_year": 1954,
                "isbn": "978-0-261-10325-7"
            },
            '2': {
                "id": '2',
                "title": "1984",
                "author": "George Orwell",
                "release_year": 1949,
                "isbn": "978-0-452-28423-4"
            }
        }
        return books.get(book_id)

    def test_it_should_be_able_to_get_a_book_by_id(self):
        self.mock_repository.get_book_by_id.side_effect = self.mock_get_book_by_id

        book = self.sut.execute(book_id='1')

        self.assertEqual(book['title'], "O Senhor dos Anéis")
        self.assertEqual(book['isbn'], "978-0-261-10325-7")

    def test_it_should_not_be_able_to_get_a_book_with_wrong_id(self):
        self.mock_repository.get_book_by_id.side_effect = self.mock_get_book_by_id

        with self.assertRaises(Exception) as context:
            self.sut.execute(book_id='wrong_book_id')

        self.assertEqual(str(context.exception), "Book not found.")
