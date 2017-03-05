from __future__ import unicode_literals

from django.db import models

class Category (models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=1000)
    product_price = models.IntegerField(default=0)
    product_category = models.ForeignKey(Category)

    def __str__(self):
        return self.product_name