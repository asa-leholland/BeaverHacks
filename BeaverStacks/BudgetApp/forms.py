from django.forms import ModelForm
from .models import Groups, Transactions, Categories, GroupTransactions, Budgets, UserTransactions, UserBudget


# This file will be used to create forms for HTML embedding of the data
class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = [
            'description',
            'budgeted',
            'spent',
            'remaining'
        ]


class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'vendor',
            'category',
            'date',
            'amount',

        ]


class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = [
            'description'
        ]


class GroupCategoryForm(ModelForm):
    class Meta:
        model = GroupTransactions
        fields = [
            'group_id',
            'category_id'
        ]


class BudgetForm(ModelForm):
    class Meta:
        model = Budgets
        fields = [
            'amount',
            'spent',
            'remaining',
            'year',
            'month'
        ]


class UserTransactionForm(ModelForm):
    class Meta:
        model = UserTransactions
        fields = [
            'user_id',
            'transaction_id',
            'category_id',
            'group_id'
        ]


class UserBudgetForm(ModelForm):
    class Meta:
        model = UserBudget
        fields = [
            'user_id',
            'budget_id',
        ]
