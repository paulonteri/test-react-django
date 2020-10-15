from django.urls import path, include
from rest_framework import routers

from .analytics_api import BooksNumApi
from .api import BookViewSet, BookInstanceViewSet, IssueBookViewSet

router = routers.DefaultRouter()
router.register('api/v2.0/library/books', BookViewSet, 'Books')
router.register('api/v2.0/library/booksissued', IssueBookViewSet, 'Issue Book')
router.register('api/v2.0/library/bookinstance', BookInstanceViewSet, 'Book Instance')

urlpatterns = [
    path('api/v2.0/library/booksnum/', BooksNumApi.as_view(), name='Books Num'),
    path('', include(router.urls)),

]
