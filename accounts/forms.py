from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegistrationForm(UserCreationForm):
    pass


class LoginForm(AuthenticationForm):
    pass
