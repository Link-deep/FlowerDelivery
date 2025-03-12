from django import forms
from .models import GamesPost

class GameForm(forms.ModelForm):
    class Meta:
        model = GamesPost
        fields = ['title', 'description', 'image', 'price', 'discount_percent', 'stock', 'platform', 'publisher', 'genre']
