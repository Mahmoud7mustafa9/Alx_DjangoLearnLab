from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

# """
# BookListView:
# - Retrieves a list of all books.
# - Accessible to all users (read-only for unauthenticated users).

# BookCreateView:
# - Allows authenticated users to create new book entries.
# - Enforces validation and permissions.

# BookUpdateView:
# - Allows authenticated users to update existing book entries.
# """

# Example:
class BookListView(generics.ListAPIView):
    # """
    # Retrieves a list of all books.
    # - Accessible to all users.
    # - Read-only for unauthenticated users.
    # """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filter by specific fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search by text
    search_fields = ['title', 'author__name']

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users
    def perform_create(self, serializer):
        # Add custom logic here if needed (e.g., log creation event)
        serializer.save()

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users
    
    
    def perform_create(self, serializer):
        # Add custom logic here if needed (e.g., log creation event)
        serializer.save()
# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users
