from django.db import models


class Livro(models.Model):
	nome = models.CharField('nome', max_length=180)
	tematica = models.CharField('temática', max_length=100)
	valor = models.DecimalField('valor', max_digits=10, decimal_places=2)

	class Meta:
		ordering = ['nome']
		verbose_name = 'livro'
		verbose_name_plural = 'livros'

	@property
	def disponivel(self):
		return not self.emprestimos.filter(status='pendente').exists()

	def __str__(self):
		return self.nome

# Create your models here.
