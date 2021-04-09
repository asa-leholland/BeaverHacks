from django.contrib import admin

# Register your models here.
from .models import Group, Category

# Current forms on the admin panel
admin.site.register(Group)
admin.site.register(Category)