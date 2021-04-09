from django.contrib import admin
from .models import Group, Category, Transactions

# Register your models here.
# Current forms on the admin panel
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Transactions)
