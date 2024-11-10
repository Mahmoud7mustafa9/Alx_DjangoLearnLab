from django.shortcuts import render
# Create your views here.
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Function-based View to list all books
def list_books (request):
    # Get all books from the database
    books = Book.objects.all()
    # Render the list in the template
    return render(request, "relationship_app/list_books.html", {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.object.books.all()
        return context
