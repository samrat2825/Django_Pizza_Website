from django.db import models

# Create your models here.

class Pizza(models.Model):
   Name = models.CharField(max_length=20)
   Img = models.ImageField(upload_to='pics')
   Type = models.CharField(max_length=10)
   Size = models.CharField(max_length=10)
   Toppings = models.CharField(max_length=10)
   Price = models.IntegerField()