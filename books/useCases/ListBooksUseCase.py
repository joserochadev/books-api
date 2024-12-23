from books.repositories.IBookRepository import IBookRepository


class ListBooksUseCase:
    def __init__(self, repository: IBookRepository):
        self.repository = repository

    def execute(self):
        books = self.repository.listBooks()

        if len(books) == 0:
            raise Exception("Books list is empty")

        return books
