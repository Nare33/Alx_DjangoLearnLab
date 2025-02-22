import datetime 
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(default=datetime.date(2025, 2, 2))

    def __str__(self):
        return self.title

