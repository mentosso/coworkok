from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from accounts.forms import RegistrationForm, LoginForm


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        raise NotImplemented()


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        raise NotImplemented()
