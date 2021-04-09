from django.forms import ModelForm
from .models import Group


# This file will be used to create forms for HTML embedding of the data
class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_description']
