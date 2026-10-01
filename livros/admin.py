from django.contrib import admin
from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
	list_display = ('nome', 'tematica', 'valor', 'status_disponibilidade')
	list_filter = ('tematica',)
	search_fields = ('nome', 'tematica')

	@admin.display(description='disponibilidade')
	def status_disponibilidade(self, obj):
		return 'Disponível' if obj.disponivel else 'Emprestado'
