# Delete Operation for Book Model

### Objective:
This operation deletes an existing `Book` instance from the database by its title.

### Command:
```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book with the title '1984'
book = Book.objects.get(title="1984")

# Delete the book instance
book.delete()

# Try to retrieve the book again (to confirm it's deleted)
Book.objects.filter(title="1984").exists()

