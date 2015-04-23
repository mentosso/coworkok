from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from accounts.forms import RegistrationForm, LoginForm


class RegistrationView(generic.FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:login')


class LoginView(generic.FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('cowork:dashboard')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy('admin:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
