from models import Author, Book , Librarian , Library 

def get_by_author (author_name, author):
    Author.objects.get(name= author_name)
    books = Author.objects.filter(author=author)
    return books

def get_in_library(library_name): 
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian(library_name):
    Librarian.objects.get(library="")
    librarian = Library.objects.librarian
    return librarian

