# bookshelf/forms.py

# BookForm validates user input for creating and updating books
# Custom validation ensures that:
# - Titles are at least 2 characters long
# - Descriptions do not contain script tags to prevent XSS attacks
# ExampleForm

# bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    # Validation for the 'title' field (just an example of custom validation)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        
        # Basic input sanitization or validation logic can be added here
        if len(title) < 2:
            raise forms.ValidationError("The title must be at least 2 characters long.")
        
        return title

    # Validation for the 'description' field
    def clean_description(self):
        description = self.cleaned_data.get('description')

        # Ensure no script tags to prevent XSS attacks
        if "<script>" in description or "</script>" in description:
            raise forms.ValidationError("Script tags are not allowed in the description.")
        
        return description
