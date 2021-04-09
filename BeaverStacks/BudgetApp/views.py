from django.shortcuts import render
from .forms import GroupForm
from .forms import TransactionsForm
from .models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    form = GroupForm()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)

def addTransaction(request):
    form = TransactionsForm()
    if request.method == 'POST':
            form = TransactionsForm(request.POST)
            if form.is_valid():
                form.save()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)

def updateTransaction(request, pk):
    transaction = Transactions.objects.get(id=pk)
    form = TransactionsForm(instance=order)
    if request.method == 'POST':
            form = TransactionsForm(request.POST, instance=transaction)
            if form.is_valid():
                form.save()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)

def deleteTransaction(request, pk):
    transaction = Transactions.objects.get(id=pk)
    if request.method == "POST":
        transaction.delete()
    form = TransactionsForm()
    context = {'item': transaction}
    return render(request, 'BudgetApp/index.html', context)