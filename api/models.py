from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Article(models.Model):
    tittle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle