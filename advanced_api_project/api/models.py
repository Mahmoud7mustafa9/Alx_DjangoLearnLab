from django.db import models

# # Create your models here.
# Create two models, Author and Book.
# The Author model should have the following fields:
# name: a string field to store the author’s name.
# The Book model should have the following fields:
# title: a string field for the book’s title.
# publication_year: an integer field for the year the book was published.
# author: a foreign key linking to the Author model, establishing a one-to-many relationship from Author to Books.
# Action Items:

# Define these models in api/models.py.
# Run migrations to create these models in the database

class Author(models.model):
    name=models.CharField(max_length=160)
    
    def __str__(self):
        return self.name

class Book(models.model):
    title= models.CharField(max_length=200)
    publication_year = models.IntegerField(max_length=20)
    author= models.ForeignKey(Author, on_delete= models.CASCADE)

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
