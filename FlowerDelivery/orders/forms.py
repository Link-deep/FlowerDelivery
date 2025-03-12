from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, initial=1, label="Количество")
    address = forms.CharField(widget=forms.Textarea, required=True, label="Адрес доставки")
    full_name = forms.CharField(required=True, label="ФИО")  # Обязательное поле
    phone = forms.CharField(required=True, label="Телефон")  # Обязательное поле

    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'quantity', 'address']  # Добавили обязательные поля
