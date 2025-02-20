import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_model.settings')

django.setup()


from relationship_app.models import Author, Book, Library, Librarian


def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")

if __name__ == '__main__':
    print("Books by a specific author:")
    books_by_author('J.K. Rowling')

    print("\nBooks in a library:")
    books_in_library('Central Library')

    print("\nLibrarian for a library:")
    librarian_for_library('Central Library')
