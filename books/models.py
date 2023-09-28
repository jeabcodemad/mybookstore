from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    nation = models.CharField(max_length=4,default='EN')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title