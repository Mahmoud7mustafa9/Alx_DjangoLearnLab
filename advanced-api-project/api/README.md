### API Endpoints
- **GET /api/books/**: List all books (accessible to all users).
- **GET /api/books/<id>/**: Retrieve details of a specific book.
- **POST /api/books/create/**: Create a new book (requires authentication).
- **PUT /api/books/<id>/update/**: Update an existing book (requires authentication).
- **DELETE /api/books/<id>/delete/**: Delete a book (requires authentication).

### Permissions
- Read operations are available to all users.
- Write operations (create, update, delete) require authentication.

### API Querying Features

1. **Filtering**
   - Filter by title: `/api/books/?title=Sample Title`
   - Filter by author name: `/api/books/?author__name=John Doe`
   - Filter by publication year: `/api/books/?publication_year=2022`

2. **Search**
   - Search for books by text in title or author name: `/api/books/?search=Python`

3. **Ordering**
   - Order by publication year (ascending): `/api/books/?ordering=publication_year`
   - Order by title (descending): `/api/books/?ordering=-title`


## Running Tests

### Test Scope
This project includes unit tests for:
- CRUD operations on the Book model.
- Filtering, searching, and ordering books via API.
- Permissions and authentication.

### Running the Test Suite
Run the following command from the project root:
```bash
python manage.py test api
