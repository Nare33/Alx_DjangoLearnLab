from django.db import models

class Author(models.Model):
    # Field to store the author's name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Field for the book's title
    title = models.CharField(max_length=200)
    # Field for the year the book was published
    publication_year = models.IntegerField()
    # ForeignKey linking the Book model to the Author model (one-to-many relationship)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
from django.db import models

class Author(models.Model):
    # Field to store the author's name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Field for the book's title
    title = models.CharField(max_length=200)
    # Field for the year the book was published
    publication_year = models.IntegerField()
    # ForeignKey linking the Book model to the Author model (one-to-many relationship)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

