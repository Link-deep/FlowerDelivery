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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'birth_date', 'address', 'avatar']

        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите телефон'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Введите адрес'}),
            'avatar': forms.FileInput(attrs={'class': 'form-file'}),
        }
