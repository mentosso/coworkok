from django import forms
from cowork.models import *


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'VAT_ID', 'website', 'company_logo')
        labels = {
            'name': 'Company name',
            'VAT_ID': 'VAT ID',
            'website': 'Website',
            'company_logo': 'Company logo'
        }


class LocationCreationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'address', 'postal_code', 'total_desks', 'reserved_desks', 'price')
