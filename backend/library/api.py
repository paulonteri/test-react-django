from rest_framework import viewsets, permissions

from .models import Book, BookInstance, IssueBook
from .serializers import BookSerializer, BookInstanceSerializer, IssueBookSerializer


#  from rest_framework.views import APIView


# class BooksViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.DjangoModelPermissions]
#     # Only authenticated users can access this API
#     serializer_class = BooksSerializer
#     queryset = Books.objects.all()
#     # permission_classes = [permissions.IsAuthenticated]
#     # # Override the get method
#     # def get_queryset(self):
#     #     # get the books belonging to this user only
#     #     return self.request.user.Books.all()
#
#     # def perform_create(self, serializer):
#     #     # save book owner while creating a book
#     #     serializer.save(owner=self.request.user)


# Book
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Book Instance
class BookInstanceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = BookInstanceSerializer
    queryset = BookInstance.objects.all()


# IssueBook
class IssueBookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    # Only authenticated users can access this API
    serializer_class = IssueBookSerializer
    queryset = IssueBook.objects.all()
