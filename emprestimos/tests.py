from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from livros.models import Livro
from usuarios.models import Usuario
from .forms import EmprestimoForm
from .models import Emprestimo


class EmprestimoTests(TestCase):
	def setUp(self):
		self.usuario = Usuario.objects.create(
			nome='Ana Lima', cpf='123.456.789-00', email='ana@example.com',
			telefone='11999990000', endereco='Rua das Flores, 10',
		)
		self.livro = Livro.objects.create(nome='Introdução à Biologia', tematica='Ciências', valor='49.90')

	def test_disponibilidade_acompanha_status(self):
		self.assertTrue(self.livro.disponivel)
		emprestimo = Emprestimo.objects.create(usuario=self.usuario, livro=self.livro)
		self.assertFalse(self.livro.disponivel)
		emprestimo.status = Emprestimo.Status.DEVOLVIDO
		emprestimo.save()
		self.assertTrue(self.livro.disponivel)

	def test_nao_permite_dois_emprestimos_pendentes_do_mesmo_livro(self):
		Emprestimo.objects.create(usuario=self.usuario, livro=self.livro)
		outro_usuario = Usuario.objects.create(
			nome='Bruno Reis', cpf='987.654.321-00', email='bruno@example.com',
			telefone='11988880000', endereco='Av. Central, 20',
		)
		duplicado = Emprestimo(usuario=outro_usuario, livro=self.livro)
		with self.assertRaises(ValidationError):
			duplicado.full_clean()

	def test_formulario_lista_somente_livros_disponiveis(self):
		Emprestimo.objects.create(usuario=self.usuario, livro=self.livro)
		form = EmprestimoForm()
		livros_no_formulario = list(form.fields['livro'].queryset)
		self.assertNotIn(self.livro, livros_no_formulario)

	def test_formularios_criam_emprestimo_e_alteram_status(self):
		response = self.client.post(reverse('emprestimos:novo'), {
			'usuario': self.usuario.pk,
			'livro': self.livro.pk,
			'data_emprestimo': '2026-10-01',
			'status': Emprestimo.Status.PENDENTE,
		})
		self.assertRedirects(response, reverse('emprestimos:lista'))
		emprestimo = Emprestimo.objects.get(livro=self.livro)

		response = self.client.post(reverse('emprestimos:status', args=[emprestimo.pk]), {
			'status': Emprestimo.Status.DEVOLVIDO,
		})
		self.assertRedirects(response, reverse('emprestimos:lista'))
		emprestimo.refresh_from_db()
		self.assertEqual(emprestimo.status, Emprestimo.Status.DEVOLVIDO)
		self.assertTrue(self.livro.disponivel)

	def test_dashboard_e_listas_estao_disponiveis(self):
		for url_name in ('inicio', 'usuarios:lista', 'livros:lista', 'emprestimos:lista'):
			with self.subTest(url=url_name):
				response = self.client.get(reverse(url_name))
				self.assertEqual(response.status_code, 200)
