from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120)
    id = models.CharField(max_length=120, primary_key=True)
    description = models.TextField(default='description default text')
    image = models.ImageField(width_field=225, height_field=225)
    category = models.CharField(max_length=120)
    price = models.IntegerField()
    quantity = models.IntegerField()
