from django import forms
from cowork.models import *


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', )
        labels = {
            'name': 'Company name'
        }


class OfficeCreationForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ('name', 'address', 'from_date', 'until_date', 'price')
