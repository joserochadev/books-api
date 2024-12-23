from django.core.management.base import BaseCommand
from books.models import Book  # Importe seus modelos
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Semeia o banco de dados com dados iniciais'

    def handle(self, *args, **kwargs):
        # Verifique se já existem dados
        if Book.objects.exists():
            self.stdout.write(self.style.WARNING(
                'O banco de dados já possui dados. Nada foi feito.'))
            return

        # Dados de exemplo para popular o banco
        books = [
            {"title": "O Senhor dos Anéis", "author": "J.R.R. Tolkien",
             "release_year": 1954, "isbn": "978-0-261-10325-7"},
            {"title": "1984", "author": "George Orwell",
             "release_year": 1949, "isbn": "978-0-452-28423-4"},
            {"title": "Dom Quixote", "author": "Miguel de Cervantes",
             "release_year": 1605, "isbn": "978-0-679-42392-3"},
            {"title": "Orgulho e Preconceito", "author": "Jane Austen",
             "release_year": 1813, "isbn": "978-0-141-43973-1"},
            {"title": "O Apanhador no Campo de Centeio", "author": "J.D. Salinger",
             "release_year": 1951, "isbn": "978-0-316-76948-0"},
        ]

        # Criar os objetos no banco de dados
        for book_data in books:
            Book.objects.create(**book_data)

        self.stdout.write(self.style.SUCCESS(
            f'{len(books)} livros adicionados com sucesso!'))
