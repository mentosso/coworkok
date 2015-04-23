from django import forms
from accounts.models import User


class RegistrationForm(forms.ModelForm):
    # TODO Add password confirm field
    class Meta:
        model = User
        fields = ['email', 'password']


class LoginForm(forms.Form):
    # TODO Copy/use authentication form from django.auth
    email = forms.CharField()
    password = forms.CharField()