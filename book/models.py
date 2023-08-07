from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.title
        
    
