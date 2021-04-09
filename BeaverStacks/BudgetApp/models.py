from django.db import models
from datetime import date


# Create your models here.
class Transaction(models.Model):
    transaction_id = models.PositiveIntegerField(default=1)
    vendor = models.CharField(default='', max_length=50)
    date = models.DateField(default=date.today)
    amount = models.DecimalField(default=0.00, max_digits=16, decimal_places=2)

    
class Group(models.Model):
    """ Model to handle main category groupings of the budget"""
    group_id = models.CharField(max_length=100)
    group_description = models.CharField(max_length=100)

    def __str__(self):
        return self.group_id


class Category(models.Model):
    """ Model that handles subcategories and maps them back to a main category"""
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    category_id = models.CharField(max_length=100)
    category_description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_id

