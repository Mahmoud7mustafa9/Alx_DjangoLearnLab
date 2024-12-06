from rest_framework import serializers
from .models import Book , Author
import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value    
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']    



"""
This file defines serializers for the Author and Book models.

BookSerializer:
- Serializes all fields of the Book model.
- Includes custom validation for the publication_year field to prevent future dates.

AuthorSerializer:
- Serializes the Author model, including a nested representation of related books.
"""
