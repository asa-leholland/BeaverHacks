from django.shortcuts import render
import requests

def index(request):
    print ("index: " + str(request.user))

    dummy_transactions = [
    {'id': 1, 'transaction_name': 'Rent/Mortgage', 'transaction_date': '2013-10-07', 'transaction_category': 'Bills', 'transaction_amount': -100.12},
    {'id': 2, 'transaction_name': 'Electric Bill', 'transaction_date': '2012-10-11', 'transaction_category': 'Bills', 'transaction_amount': -120.12},
    {'id': 3, 'transaction_name': 'Gas', 'transaction_date': '2013-11-07', 'transaction_category': 'Bills', 'transaction_amount': -10.12},
    {'id': 4, 'transaction_name': 'Netflix Subscription', 'transaction_date': '2031-10-07', 'transaction_category': 'Entertainment', 'transaction_amount': -170.12},
    {'id': 5, 'transaction_name': 'Paycheck', 'transaction_date': '2021-10-02', 'transaction_category': 'Income', 'transaction_amount': +1200.12},
    {'id': 6, 'transaction_name': 'Tuition', 'transaction_date': '2022-10-09', 'transaction_category': 'Education', 'transaction_amount': -120.19}
    ]


    context = {'hello': 'world', 'transactions': dummy_transactions}
    return render(request, 'index.html', context)