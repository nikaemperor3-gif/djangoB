from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Emprestimo(models.Model):
	class Status(models.TextChoices):
		PENDENTE = 'pendente', 'Pendente'
		DEVOLVIDO = 'devolvido', 'Devolvido'
		EXPIRADO = 'expirado', 'Expirado'

	usuario = models.ForeignKey(
		'usuarios.Usuario', on_delete=models.PROTECT, related_name='emprestimos',
		verbose_name='usuário',
	)
	livro = models.ForeignKey(
		'livros.Livro', on_delete=models.PROTECT, related_name='emprestimos',
		verbose_name='livro',
	)
	data_emprestimo = models.DateField('data do empréstimo', default=timezone.localdate)
	status = models.CharField('status', max_length=10, choices=Status.choices, default=Status.PENDENTE)

	class Meta:
		ordering = ['-data_emprestimo', '-pk']
		verbose_name = 'empréstimo'
		verbose_name_plural = 'empréstimos'
		constraints = [
			models.UniqueConstraint(
				fields=['livro'], condition=Q(status='pendente'), name='um_emprestimo_pendente_por_livro'
			)
		]

	def clean(self):
		super().clean()
		if self.status == self.Status.PENDENTE and self.livro_id:
			outros_pendentes = Emprestimo.objects.filter(
				livro_id=self.livro_id, status=self.Status.PENDENTE
			).exclude(pk=self.pk)
			if outros_pendentes.exists():
				raise ValidationError({'livro': 'Este livro já possui um empréstimo pendente.'})

	def __str__(self):
		return f'{self.livro} - {self.usuario} ({self.get_status_display()})'

# Create your models here.
