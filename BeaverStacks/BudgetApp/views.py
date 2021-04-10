from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.
def base(request, *args, **kwargs):
    print(*args)
    print(**kwargs)
    form = BudgetForm()
    context = {'form': form}
    return render(request, 'base.html', context)


def index(request):
    groups = GroupForm()
    categories = CategoryForm()
    budgets = BudgetForm()
    transactions = Transactions()

    if request.method == 'POST':
        if request.POST.get('transaction_description'):
            create_transaction(request, transactions)
        if request.POST.get('category_description'):
            create_category(request, categories)
        if request.POST.get('group_description'):
            create_group(request, groups)

    # This Works
    # if request.POST['Category']:
    #     print(request.POST['Category'])
    #     categories = create_category(request, categories)
    transactions = Transactions.objects.all()  # this is a list of all the transactions in the db
    categories = Categories.objects.all()  # this is a list of all the categories in the db
    groups = Groups.objects.all()  # this is a list of all the groups in the db
    context = {
        'month_year_combinations': get_month_year_combinations(),
        'budgets': budgets,
        'transactions': transactions,
        'categories': categories,
        'groups': groups
    }
    return render(request, 'index.html', context)


def get_month_year_combinations():
    # form = BudgetForm()
    budget_list = ['May 2017', 'June 2017', 'July 2017']
    # for budget_item in form:
    #     budget_list.append(str(budget_item.month) + str(budget_item.year))
    return budget_list


def create_transaction(request, transactions):
    transaction = Transactions()
    transaction.transaction_description = request.POST.get('transaction_description')
    transaction.vendor = request.POST.get('vendor')
    transaction.category = request.POST.get('category')
    transaction.date = request.POST.get('date')
    transaction.amount = request.POST.get('amount')
    transaction.save()


def update_transaction(request, pk):
    transaction = Transactions.objects.get(id=pk)
    form = TransactionsForm(instance=transaction)
    if request.method == 'POST':
        form = TransactionsForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def delete_transaction(request, pk):
    transaction = Transactions.objects.get(id=pk)
    if request.method == "POST":
        transaction.delete()
    form = TransactionsForm()
    context = {'item': transaction}
    return render(request, 'BudgetApp/index.html', context)


def create_group(request):
    """ Creates a new group """
    form = GroupForm()

    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def update_group(request, pk):
    """ Updates a Group - needs a primary key (pk) which should be linked to urls"""
    group = Groups.objects.get(id=pk)
    form = GroupForm(instance=group)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def delete_group(request, pk):
    """ Deletes a Group - also needs a pk"""
    group = Groups.objects.get(id=pk)
    if request.method == 'POST':
        group.delete()
    context = {'item': group}  # 'item' will need to be updated to what the object is in the template
    return render(request, 'BudgetApp/index.html', context)


def create_category(request, form):
    """ Creates a new Category """
    print('Called')
    if request.method == 'POST':
        print('entered')
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return context


def update_category(request, pk):
    """ Updates a Category - needs a primary key (pk) which should be linked to urls"""
    category = Categories.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def delete_category(request, pk):
    """ Deletes a Category - also needs a pk"""
    category = Categories.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
    context = {'item': category}  # 'item' will need to be updated to what the object is in the template
    return render(request, 'BudgetApp/index.html', context)
