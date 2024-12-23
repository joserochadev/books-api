from books.repositories.IBookRepository import IBookRepository


class RemoveBookUseCase:
    def __init__(self, repository: IBookRepository):
        self.repository = repository

    def execute(self, book_id: str):
        book = self.repository.get_book_by_id(book_id)

        if not book:
            raise Exception("Book not found.")

        self.repository.remove_book(book_id)
