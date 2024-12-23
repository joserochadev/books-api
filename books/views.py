from pydantic import UUID4, BaseModel, StrictInt, StrictStr, ValidationError
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response

from .repositories.booksRepositories.BookRepository import BookRepository
from .serializer import BookSerializer
from .useCases.CreateBookUseCase import CreateBookUseCase
from .useCases.GetBookUseCase import GetBookUseCase
from .useCases.ListBooksUseCase import ListBooksUseCase
from .useCases.RemoveBookUseCase import RemoveBookUseCase


class CreateBookBodySchema(BaseModel):
    title: StrictStr
    author: StrictStr
    release_year: StrictInt
    isbn: StrictStr


class BookIdSchema(BaseModel):
    book_id: UUID4


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_books(request: Request) -> Response:
    book_repository = BookRepository()
    list_book_usecase = ListBooksUseCase(book_repository)

    try:
        books = list_book_usecase.execute()
        serializer = BookSerializer(books, many=True)
        return Response(data={'book': serializer.data})
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_book(request: Request) -> Response:

    book_repository = BookRepository()
    create_book_usecase = CreateBookUseCase(book_repository)

    try:
        book_schema = CreateBookBodySchema(**request.data)
        book = create_book_usecase.execute(book_schema)

        serializer = BookSerializer(book)

        return Response(data={'book': serializer.data}, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response(data={'message': str(e.errors())}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_book_by_id(request: Request, book_id: str) -> Response:
    book_repository = BookRepository()
    get_book_usecase = GetBookUseCase(book_repository)

    try:
        book_id_schema = BookIdSchema(book_id=book_id)
        book = get_book_usecase.execute(book_id_schema.book_id)
        serializer = BookSerializer(book)

        return Response(data={'book': serializer.data})

    except ValidationError as e:
        return Response(data={'message': str(e.errors())}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def remove_book(request: Request, book_id: str):
    book_repository = BookRepository()
    remove_book_usecase = RemoveBookUseCase(book_repository)

    try:
        book_id_schema = BookIdSchema(book_id=book_id)
        remove_book_usecase.execute(book_id_schema.book_id)

        return Response(data={'message': 'Book deleted successfully'})
    except ValidationError as e:
        return Response(data={'message': str(e.errors())}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
