from django import forms
from cowork.models import Company


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', )
        labels = {
            'name': 'Company name'
        }