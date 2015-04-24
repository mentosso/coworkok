from django.shortcuts import redirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from accounts.forms import UserCreationForm, LoginForm
from accounts.const import *
from cowork.forms import CompanyCreationForm


class RegistrationView(generic.TemplateView):
    """
    Special kind of view for handling more than one
    form at once. It simply uses prefixes on forms.
    """
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('cowork:dashboard')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user_form = UserCreationForm(prefix="user")
        company_form = CompanyCreationForm(prefix="company")
        context.update({'user_form': user_form,
                        'company_form': company_form})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user_form = UserCreationForm(request.POST, prefix="user")
        company_form = CompanyCreationForm(request.POST, prefix="company")
        forms_valid = False

        if user_form.is_valid():
            user = user_form.save(commit=False)
            if user.user_type == USER_TYPE_COMPANY:
                if company_form.is_valid():
                    company = company_form.save(commit=False)
                    user.save()
                    company.user = user
                    company.save()
                    forms_valid = True
            else:
                forms_valid = True
                user.save()
            if forms_valid:
                user = authenticate(username=user_form.cleaned_data['email'],
                                    password=user_form.cleaned_data['password1'])
                login(self.request, user)
                return redirect('cowork:dashboard')

        context = self.get_context_data(**kwargs)
        context.update({'user_form': user_form,
                        'company_form': company_form})
        return self.render_to_response(context)


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
    url = reverse_lazy('index')
    permanent = False

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
