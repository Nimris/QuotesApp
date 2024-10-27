from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name='quotes')
    tags = models.ManyToManyField('Tag')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')
    is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.quote}"
    

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    born_date = models.DateField()
    born_location = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name}"
    

class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    quotes = models.ManyToManyField('Quote')

    def __str__(self):
        return f"{self.name}"
    
    
    
    