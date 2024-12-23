from unittest.mock import MagicMock

from django.test import TestCase

from books.repositories.IBookRepository import IBookRepository
from books.useCases.RemoveBookUseCase import RemoveBookUseCase


class TestRemoveBookUseCase(TestCase):

    def setUp(self):
        self.mock_repository = MagicMock(spec=IBookRepository)
        self.sut = RemoveBookUseCase(self.mock_repository)

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

    def test_it_should_be_able_to_remove_a_book_by_id(self):
        self.mock_repository.get_book_by_id.side_effect = self.mock_get_book_by_id

        book_id = '1'

        self.sut.execute(book_id)

        self.mock_repository.get_book_by_id.assert_called_once_with(
            book_id)
        self.mock_repository.remove_book.assert_called_once_with(book_id)

    def test_it_should_raise_exception_if_book_does_not_exists(self):
        self.mock_repository.get_book_by_id.side_effect = self.mock_get_book_by_id

        book_id = 'invalid_id'

        with self.assertRaises(Exception) as context:
            self.sut.execute(book_id)

        self.assertEqual(str(context.exception), "Book not found.")
        self.mock_repository.remove_book.assert_not_called()
