from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=100)
    author  = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['author'],
        unique_together = (('title', 'author'))
        unique_together = (('isbn',))

    def __str__(self):
        return f'{self.title} by {self.author} (ISBN: {self.isbn})'