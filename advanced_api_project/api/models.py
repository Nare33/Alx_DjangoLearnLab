from django.db import models

class Author(models.Model):
    """
    Represents an author with a name.
    Each author can have multiple books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with a title, publication year, and associated author.
    A book is linked to a single author but an author can have multiple books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)

    def __str__(self):
        return self.title

