from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, BookInstance, IssueBook


class BooksNumApi(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        book_titles = Book.objects.all().count()
        book_instances = BookInstance.objects.all().count()
        books_issued = IssueBook.objects.filter(available=False).count()
        books_available = book_instances - books_issued
        return Response({
            "total_books": book_titles,
            "total_book_instances": book_instances,
            "books_issued": books_issued,
            "books_available": books_available
        })

    def post(self, request, format=None, *args, **kwargs):
        return Response(request.data["qwe"])
