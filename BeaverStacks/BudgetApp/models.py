from django.db import models


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
