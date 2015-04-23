from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)


class LoginForm(AuthenticationForm):
    pass
