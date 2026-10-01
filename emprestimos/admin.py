from django.contrib import admin
from .models import Emprestimo


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'livro', 'data_emprestimo', 'status')
	list_filter = ('status', 'data_emprestimo')
	search_fields = ('usuario__nome', 'usuario__cpf', 'livro__nome')
	autocomplete_fields = ('usuario', 'livro')
