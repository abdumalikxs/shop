from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def product_count(self):
        return self.product_set.count()


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    in_stock = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
