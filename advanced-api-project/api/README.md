### API Endpoints
- **GET /api/books/**: List all books (accessible to all users).
- **GET /api/books/<id>/**: Retrieve details of a specific book.
- **POST /api/books/create/**: Create a new book (requires authentication).
- **PUT /api/books/<id>/update/**: Update an existing book (requires authentication).
- **DELETE /api/books/<id>/delete/**: Delete a book (requires authentication).

### Permissions
- Read operations are available to all users.
- Write operations (create, update, delete) require authentication.
