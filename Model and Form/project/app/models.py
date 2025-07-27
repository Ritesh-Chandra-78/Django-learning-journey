from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
