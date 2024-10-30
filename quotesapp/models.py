from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='quotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes', default=1)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.quote}"
    

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    born_date = models.TextField()
    born_location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    is_default=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"
    
    
    
    