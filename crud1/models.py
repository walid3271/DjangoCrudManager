from django.db import models

# Create your models here.
class user_model(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    textbox = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name