from django.db import models

# Create your models here.
class Product(models.Model):
    item = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()