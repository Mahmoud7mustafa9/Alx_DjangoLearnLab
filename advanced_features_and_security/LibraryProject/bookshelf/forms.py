# bookshelf/forms.py

# BookForm validates user input for creating and updating books
# Custom validation ensures that:
# - Titles are at least 2 characters long
# - Descriptions do not contain script tags to prevent XSS attacks
# ExampleForm