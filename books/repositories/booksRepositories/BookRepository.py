from books.models import Book
from books.repositories.IBookRepository import IBookRepository


class BookRepository(IBookRepository):
    def create_book(self, data):
        book = Book.objects.create(
            title=data.title,
            author=data.author,
            release_year=data.release_year,
            isbn=data.isbn,
        )

        return book

    def get_book_by_isbn(self, isbn):
        return Book.objects.filter(isbn=isbn).first()

    def listBooks(self):
        return Book.objects.all()

    def get_book_by_id(self, id):
        return Book.objects.filter(id=id).first()

    def remove_book(self, id):
        Book.objects.get(id=id).delete()
