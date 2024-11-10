from django.shortcuts import render
# Create your views here.
from .models import Book
from .models import Library
from django.views.generic import ListView

# Function-based View to list all books
def list_books(request):
    # Get all books from the database
    books = Book.objects.all()
    # Render the list in the template
    return render(request, "relationship_app/list_books.html", {'books': books})

class LibraryDetailView(ListView):
    model = Book
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'books'

    def get_queryset(self):
        # Get the library by the ID passed in the URL and then return books for that library
        library_id = self.kwargs['library_id']
        return Book.objects.filter(library__id=library_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library_id = self.kwargs['library_id']
        library = Library.objects.get(id=library_id)
        context['library'] = library
        return context
