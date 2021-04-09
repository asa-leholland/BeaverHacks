from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


# Create your models here.


class Group(models.Model):
    """ Model to handle main category groupings of the budget"""
    group_id = models.CharField(max_length=100)
    group_description = models.CharField(max_length=100)

    def __str__(self):
        return self.group_id
    
    
class Category(models.Model):
    """ Model that handles subcategories and maps them back to a main category"""
    group_Id = models.ForeignKey(Group, on_delete=models.CASCADE)
    category_id = models.CharField(max_length=100)
    category_description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_id


class GroupCategories(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
class Transactions(models.Model):
    transaction_id = models.PositiveIntegerField(default=1)
    vendor = models.CharField(default='', max_length=50)
    date = models.DateField(default=date.today)
    amount = models.DecimalField(default=0.00, max_digits=16, decimal_places=2)


class Budget(models.Model):
    budget_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    spent = models.DecimalField(max_digits=16, decimal_places=2)
    remaining = models.DecimalField(max_digits=16, decimal_places=2)


class UserTransactions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)


class UserBudget(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    year = models.DateTimeField(default=timezone.now().year)
    month = models.DateField(default=timezone.now().month)

