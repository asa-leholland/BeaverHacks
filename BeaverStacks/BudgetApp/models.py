from django.db import models
from datetime import date

# Create your models here.
class Transaction(models.Model):
    transaction_id = models.PositiveIntegerField(default=1)
    vendor = models.CharField(default='', max_length=50)
    date = models.DateField(default=date.today)
    amount = models.DecimalField(default=0.00, max_digits=16, decimal_places=2)


