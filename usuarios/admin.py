from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cpf', 'email', 'telefone')
	search_fields = ('nome', 'cpf', 'email')
