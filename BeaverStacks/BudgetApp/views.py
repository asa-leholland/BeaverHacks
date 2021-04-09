from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.
def index(request):
    form = GroupForm()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def createGroup(request):
    """ Creates a new group """
    form = GroupForm()

    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def updateGroup(request, pk):
    """ Updates a Group - needs a primary key (pk) which should be linked to urls"""
    group = Group.objects.get(id=pk)
    form = GroupForm(instance=group)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def deleteGroup(request, pk):
    """ Deletes a Group - also needs a pk"""
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        group.delete()
    context = {'item': group}  # 'item' will need to be updated to what the object is in the template
    return render(request, 'BudgetApp/index.html', context)


def createCategory(request):
    """ Creates a new Category """
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def updateCategory(request, pk):
    """ Updates a Category - needs a primary key (pk) which should be linked to urls"""
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)


def deleteCategory(request, pk):
    """ Deletes a Category - also needs a pk"""
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
    context = {'item': category}  # 'item' will need to be updated to what the object is in the template
    return render(request, 'BudgetApp/index.html', context)
