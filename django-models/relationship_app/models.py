from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete= models.CASCADE )
    def __str__(self):
        return self.title

class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book,related_name= name)
    def __str__(self):
        return self.name
class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library = models.OneToOneField(Library)
    def __str__(self):
        return self.name 

# Author Model:
# name: CharField.
# Book Model:,
# title: CharField.
# author: ForeignKey to Author.

# Library Model:
# name: CharField.
# books: ManyToManyField to Book.

# Librarian Model:
# name: CharField.
# library: OneToOneField to Library.

# Apply Database Migrations:

# Run migrations to create your model tables: python manage.py makemigrations relationship_app followed by python manage.py migrate.
# Implement Sample Queries:

# Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.