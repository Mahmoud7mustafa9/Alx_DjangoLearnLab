from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    # URL pattern for the function-based view to list all books
    path('list_books/', list_books , name='list_books'),

    # URL pattern for the class-based view to display books in a specific library
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
]