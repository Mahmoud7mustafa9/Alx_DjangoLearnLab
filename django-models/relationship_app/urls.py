from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # URL pattern for the function-based view to list all books
    path('books/', views.list_books , name='book_list'),

    # URL pattern for the class-based view to display books in a specific library
    path('library/<int:library_id>/', views.LibraryDetailView.as_view(), name='library_detail'),
]