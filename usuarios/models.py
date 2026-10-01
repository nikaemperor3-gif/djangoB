from django.db import models


class Usuario(models.Model):
	nome = models.CharField('nome', max_length=150)
	cpf = models.CharField('CPF', max_length=14, unique=True)
	email = models.EmailField('e-mail')
	telefone = models.CharField('telefone', max_length=25)
	endereco = models.CharField('endereço', max_length=255)

	class Meta:
		ordering = ['nome']
		verbose_name = 'usuário'
		verbose_name_plural = 'usuários'

	def __str__(self):
		return self.nome

# Create your models here.
