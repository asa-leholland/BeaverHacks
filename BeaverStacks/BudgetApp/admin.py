from django.contrib import admin
from .models import Groups, Categories, Transactions, GroupCategories

# Register your models here.
# Current forms on the admin panel
admin.site.register(Groups)
admin.site.register(Categories)
admin.site.register(Transactions)
admin.site.register(GroupCategories)