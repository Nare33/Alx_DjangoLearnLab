from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    Fields:
        name: The name of the author (string).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    Fields:
        title: The title of the book (string).
        publication_year: The year the book was published (integer).
        author: A foreign key linking to the Author model.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

