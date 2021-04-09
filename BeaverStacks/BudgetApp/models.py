from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Groups(models.Model):
    groupId = models.IntegerField()
    groupDescription = models.TextField()


class Categories(models.Model):
    categoryId = models.IntegerField()
    categoryDescription = models.TextField()


class GroupCategories(models.Model):
    groupId = models.ForeignKey(Groups, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)


class Transaction(models.Model):
    transactionId = models.IntegerField()
    vendor = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(default=timezone.now)


class Budget(models.Model):
    budgetId = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent = models.DecimalField(max_digits=10, decimal_places=2)
    remaining = models.DecimalField(max_digits=10, decimal_places=2)


class UserTransactions(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    transactionId = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)
    groupId = models.ForeignKey(Groups, on_delete=models.CASCADE)


class UserBudget(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    budgetId = models.ForeignKey(Budget, on_delete=models.CASCADE)
    year = models.DateTimeField(default=timezone.now().year)
    month = models.DecimalField(default=timezone.now().month)