from django.forms import ModelForm
from .models import Groups
from .models import Transactions


# This file will be used to create forms for HTML embedding of the data
class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['group_description']

class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['vendor', 'date', 'amount']