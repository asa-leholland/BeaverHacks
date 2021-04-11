"""
# Developed for BeaverHacks Hackathon
# Developers: Kenneth Street, Asa Holland, Charlie Magill, Jacob Ogle
"""


from .models import Categories, Groups, Budgets, Transactions, GroupCategories
from django.utils import timezone
from django.shortcuts import render
from .forms import *
import datetime


# Create your views here.
def base(request):
    return render(request, 'base.html', {})


def index(request):
    current_year = timezone.now().year
    current_month_num = timezone.now().month
    current_month_name = datetime.date.today()
    current_month = current_month_name.strftime("%B")
    print(current_month_num)
    # Populate Objects by month / year

    categories = Categories()
    groups = Groups()
    transactions = Transactions()
    budgets = Budgets()


    if request.method == 'POST':
        if request.POST.get('create_budget'):
            create_budget(request, budgets)

        if request.POST.get('create_category'):
            create_category(request, categories)

        if request.POST.get('create_group'):
            create_group(request, groups)

        if request.POST.get('create_transaction'):
            create_transaction(request, transactions)

        if request.POST.get('update_category'):
            update_category(request, request.POST.get('primary_key'))

        if request.POST.get('update_group'):
            update_group(request, request.POST.get('primary_key'))

        if request.POST.get('update_transaction'):
            update_transaction(request, request.POST.get('primary_key'))

        if request.POST.get('delete_category'):
            delete_category(request, request.POST.get('primary_key'))

        if request.POST.get('delete_group'):
            delete_group(request, request.POST.get('primary_key'))

        if request.POST.get('delete_transaction'):
            delete_transaction(request, request.POST.get('primary_key'))

    # this is a list of all the objects in the db
    budget = get_budget_by_month_year(current_month_num, current_year)
    transactions = Transactions.objects.all()
    categories = Categories.objects.all()
    groups = Groups.objects.all()
    group_categories = GroupCategories.objects.all()

    context = {
        # 'month_year_combinations': get_month_year_combinations(),
        'month': current_month,
        'year': current_year,
        'budget': budget,
        'transactions': transactions,
        'categories': categories,
        'groups': groups,
        'group_categories': group_categories
    }
    return render(request, 'index.html', context)


def create_category(request, categories):
    """ Creates a new Category """
    categories.description = request.POST.get('category_description')
    categories.budgeted = request.POST.get('category_budgeted')
    categories.save()

    group = get_group(request.POST.get('category_group'))
    print(group.id)
    create_group_category(group, categories)


def create_group_category(group, category):  # group and category need to be objects
    print(group.id)
    group_category = GroupCategories()
    group_category.group_id = group
    group_category.category_id = category
    group_category.save()


def create_group(request, groups):
    """ Creates a new Group """
    groups.description = request.POST.get('group_description')
    groups.save()

def create_budget(request, budgets):
    """ Creates a new Budget """
    budgets.amount = request.POST.get('budget_amount')
    budgets.spent = request.POST.get('budget_amount')
    budgets.remaining = request.POST.get('budget_amount')
    budgets.year = datetime.date.today()
    budgets.month = datetime.date.today()
    budgets.save()


def create_transaction(request, transactions):
    """ Creates a new Transaction """
    transactions.description = request.POST.get('transaction_description')
    transactions.vendor = request.POST.get('transaction_vendor')
    transactions.category = request.POST.get('transaction_category')
    transactions.date = request.POST.get('transaction_date')
    transactions.amount = request.POST.get('transaction_amount')
    transactions.save()


def delete_category(request, pk):
    """ Deletes a Category - needs a primary key """
    category = Categories.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()


def delete_group(request, pk):
    """ Deletes a Group - needs a primary key """
    group = Groups.objects.get(id=pk)
    if request.method == 'POST':
        group.delete()


def delete_budget(request, pk):
    """ Deletes a Budget - needs a primary key """
    budget = Budgets.objects.get(id=pk)
    if request.method == 'POST':
        budget.delete()


def delete_transaction(request, pk):
    """ Deletes a Transaction - needs a primary key """
    transaction = Transactions.objects.get(id=pk)
    if request.method == 'POST':
        transaction.delete()


def update_category(request, pk):
    """ Updates a Category - needs a primary key"""
    category = Categories.objects.get(id=pk)
    if request.method == 'POST':
        create_category(request, category)


def update_group(request, pk):
    """ Updates a Group - needs a primary key (pk) which should be linked to urls"""
    group = Groups.objects.get(id=pk)
    if request.method == 'POST':
        group.description = request.POST.get('group_description')
        group.save()


def update_budget(request, pk):
    """ Updates a Budget - needs a primary key"""
    budget = Budgets.objects.get(id=pk)
    if request.method == 'POST':
        create_budget(request, budget)


def update_transaction(request, pk):
    transaction = Transactions.objects.get(id=pk)
    if request.method == 'POST':
        create_transaction(request, transaction)


def get_month_year_combinations():
    # form = BudgetForm()
    budget_list = ['May 2017', 'June 2017', 'July 2017']
    # for budget_item in form:
    #     budget_list.append(str(budget_item.month) + str(budget_item.year))
    return budget_list


def get_budget_by_month_year(month, year):
    budgets = Budgets.objects.all()
    for budget in budgets:
        if budget.year.year == year and budget.month.month == month:
            return budget


# def buget_exists():
#     budgets = Budgets.objects.all()
#     for budget in budgets:
#         print(month)
#         if budget.year.year == year and budget.month.month == month:
#             print(budget)
#             return budget


def get_transaction_sum_by_month_year(month, year):
    transactions = Transactions.objects.all()
    total_spent = 0

    for transaction in transactions:
        if transaction.date.strftime("%M") == month and transaction.date.strftime("%Y") == year:
            total_spent += transaction.amount
    return total_spent


def update_groups_budget(group, amount):
    group.spent += amount


def get_group(description):
    for group in Groups.objects.all():
        if group.description == description:
            return group

