"""
# Developed for BeaverHacks Hackathon
# Developers: Kenneth Street, Asa Holland, Charlie Magill, Jacob Ogle
"""
import re

from .models import Categories, Groups, Budgets, Transactions
from django.utils import timezone
from django.shortcuts import render
from .forms import *
import plotly.express as px
import pandas as pd


# Create your views here.
def base(request):
    return render(request, 'base.html', {})


def index(request):
    current_year = timezone.now().year
    current_month = timezone.now().month
    categories = Categories()
    groups = Groups()
    transactions = Transactions()
    budgets = Budgets()

    getting_transaction_data()
    manipulating_transaction_data()

    if request.method == 'POST':
        if request.POST.get('create_budget'):
            create_budget(request, budgets)
        if request.POST.get('create_category'):
            create_category(request, categories)
        if request.POST.get('create_group'):
            create_group(request, groups)
        if request.POST.get('update_category'):
            update_category(request, request.POST.get('primary_key'))
        if request.POST.get('update_group'):
            update_group(request, request.POST.get('primary_key'))
        if request.POST.get('delete_category'):
            delete_category(request, request.POST.get('primary_key'))
        if request.POST.get('delete_group'):
            delete_group(request, request.POST.get('primary_key'))
        if request.POST.get('create_pie_plot'):
            create_pie_plot(request)

    # this is a list of all the objects in the db
    budgets = Budgets.objects.all()
    transactions = Transactions.objects.all()
    categories = Categories.objects.all()
    groups = Groups.objects.all()

    context = {
        'month_year_combinations': get_month_year_combinations(),
        'budgets': budgets,
        'transactions': transactions,
        'categories': categories,
        'groups': groups
    }
    return render(request, 'index.html', context)


def create_category(request, categories):
    """ Creates a new Category """
    categories.description = request.POST.get('category_description')
    categories.save()


def create_group(request, groups):
    """ Creates a new Group """
    groups.description = request.POST.get('group_description')
    groups.save()


def create_budget(request, budgets):
    """ Creates a new Budget """
    budgets.amount = request.POST.get('budget_amount')
    budgets.spent = request.POST.get('budget_spent')
    budgets.remaining = request.POST.get('budget_remaining')
    budgets.year = request.POST.get('budget_year')
    budgets.month = request.POST.get('budget_month')
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


def getting_transaction_data():
    print('function called')
    transactions = Transactions.objects.all()
    transaction_category = []
    transaction_amount = []
    for transaction in transactions:
        transaction_category.append(transaction.get_category())
        transaction_amount.append(transaction.get_amount())
    transaction_data = list(zip(transaction_category, transaction_amount))
    return transaction_data


def manipulating_transaction_data():
    data = getting_transaction_data()
    data_groupings = {}
    for i in data:
        if i[0] in data_groupings:
            data_groupings[f'{i[0]}'] += i[1]
        else:
            data_groupings[f'{i[0]}'] = i[1]

    data_for_charts = []
    for key, value in data_groupings.items():
        temp = [key, value]
        data_for_charts.append(temp)

    cats = [i[0] for i in data_for_charts]
    print(cats)
    amount = [i[1] for i in data_for_charts]
    amount_filter = []
    for i in amount:
        amount_filter.append((re.findall(r'[+-]?([0-9]*[.])?[0-9]+', str(i))))

    print(amount_filter)
    amount_filter = [float(i[0]) for i in amount_filter]
    print(amount_filter)
    final_dict = {'Category': cats, 'Amount': amount_filter}
    df = pd.DataFrame.from_dict(final_dict)
    return df


def create_pie_plot(request):
    fig = px.pie(manipulating_transaction_data(), values='Amount', names='Category', title='Spending by Category')
    fig.show()
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    return graph

