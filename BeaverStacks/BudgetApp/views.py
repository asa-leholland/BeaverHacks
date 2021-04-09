from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.
def index(request):
    form = GroupForm()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def add_transaction(request):
    form = TransactionsForm()
    if request.method == 'POST':
        form = TransactionsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


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


def create_category(request):
    """ Creates a new Category """
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


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
