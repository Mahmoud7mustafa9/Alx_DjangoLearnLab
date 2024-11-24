from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




# api/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# BookViewSet handles CRUD operations on the Book model
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # This is the data set we will operate on
    serializer_class = BookSerializer  # Serializer to format the data into JSON
