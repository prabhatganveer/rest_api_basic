from django.db import   models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50,blank=True)
    author=models.CharField(max_length=50,blank=True)
    isbn=models.CharField(max_length=50,blank=True)
    publisher=models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.title
    