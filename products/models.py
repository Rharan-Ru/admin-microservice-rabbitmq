from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
