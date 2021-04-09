from django.forms import ModelForm
from .models import Groups


# This file will be used to create forms for HTML embedding of the data
class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['group_description']
