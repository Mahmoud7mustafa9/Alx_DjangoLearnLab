from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# """
# This file defines the data models for the API.

# Author:
# - Represents a book author.
# - Fields:
#   - name: The author's name.

# Book:
# - Represents a book.
# - Fields:
#   - title: The book's title.
#   - publication_year: Year of publication.
#   - author: A foreign key to the Author model, creating a one-to-many relationship.
# """
