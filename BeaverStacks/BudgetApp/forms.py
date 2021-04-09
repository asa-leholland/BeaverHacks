from django.forms import ModelForm
from .models import Groups, Categories, GroupCategories, Transactions, Budgets, UserTransactions, UserBudget


# This file will be used to create forms for HTML embedding of the data
class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['group_description']


class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['category_id, category_description']


class GroupCategoryForm(ModelForm):
    class Meta:
        model = GroupCategories
        fields = ['group_id, category_id']


class BudgetForm(ModelForm):
    class Meta:
        model = Budgets
        fields = ['vendor, date, amount']


class UserTransactionForm(ModelForm):
    class Meta:
        model = UserTransactions
        fields = ['user_id, transaction_id, category_id, group_id']


class UserBudgetForm(ModelForm):
    class Meta:
        model = UserBudget
        fields = ['user_id, budget_id, year, month']
