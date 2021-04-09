from django.shortcuts import render
from .forms import GroupForm, CategoryForm, GroupCategoryForm, BudgetForm, UserTransactionForm, UserBudgetForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    form = GroupForm()
    context = {'form': form}
    return render(request, 'BudgetApp/index.html', context)
