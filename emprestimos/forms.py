from django import forms
from .models import Emprestimo


class EmprestimoForm(forms.ModelForm):
    data_emprestimo = forms.DateField(
        label='data do empréstimo',
        localize=False,
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    )

    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro', 'data_emprestimo', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        livros_disponiveis = Emprestimo.objects.filter(status=Emprestimo.Status.PENDENTE).values('livro_id')
        self.fields['livro'].queryset = self.fields['livro'].queryset.exclude(pk__in=livros_disponiveis)


class StatusEmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['status']
