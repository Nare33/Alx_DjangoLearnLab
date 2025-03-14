# Advanced API Project

This project implements an API for managing Authors and Books using Django REST Framework.

## Models

-   **Author:**
    -   `name`: String
-   **Book:**
    -   `title`: String
    -   `publication_year`: Integer
    -   `author`: ForeignKey to Author

## API Endpoints

-   `/api/books/`: List all books (GET)
-   `/api/books/<int:pk>/`: Retrieve a single book (GET)
-   `/api/books/create/`: Create a new book (POST)
-   `/api/books/<int:pk>/update/`: Update a book (PUT/PATCH)
-   `/api/books/<int:pk>/delete/`: Delete a book (DELETE)

## Advanced Query Capabilities

The BookListView now supports advanced query capabilities, including filtering, searching, and ordering.

### Filtering

Users can filter books by title, author, and publication year using query parameters.

Example:

-   `/api/books/?title=Pride and Prejudice`
-   `/api/books/?author=1` (where 1 is the author's ID)
-   `/api/books/?publication_year=1813`

### Searching

Users can search for books by title or author name using the `search` query parameter.

Example:

-   `/api/books/?search=Pride` (searches for 'Pride' in titles and author names)

### Ordering

Users can order books by title or publication year using the `ordering` query parameter.

Example:

-   `/api/books/?ordering=title` (orders by title in ascending order)
-   `/api/books/?ordering=-publication_year` (orders by publication year in descending order)
