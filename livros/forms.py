from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'tematica', 'valor']
        widgets = {'valor': forms.NumberInput(attrs={'step': '0.01', 'min': '0'})}
