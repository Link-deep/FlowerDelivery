from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
