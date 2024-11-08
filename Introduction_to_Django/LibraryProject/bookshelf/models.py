from django.db import models

# Create your models here.
class Book (models.model):
    title= models.CharField(max_length=200)
    author= models.CharField(max_length=100)
    publication_year = models.DateField()


#     title: CharField with a maximum length of 200 characters.
# author: CharField with a maximum length of 100 characters.
# publication_year: IntegerField.

# def __str__(self):
#         return self.title
book = Book(
    title="1984",
    author="George Orwell",
    publication_year= 1949
)
all_books = Book.objects.all()
book2 = Book.objects.get(title="1964")
book2.title= "new elephant"
book2.save()
book2.delete()
