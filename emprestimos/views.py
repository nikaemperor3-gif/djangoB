from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from livros.models import Livro
from usuarios.models import Usuario
from .forms import EmprestimoForm, StatusEmprestimoForm
from .models import Emprestimo


class DashboardView(ListView):
	model = Emprestimo
	template_name = 'inicio.html'
	context_object_name = 'emprestimos_recentes'

	def get_queryset(self):
		return Emprestimo.objects.select_related('usuario', 'livro')[:8]

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			'total_usuarios': Usuario.objects.count(),
			'total_livros': Livro.objects.count(),
			'livros_disponiveis': sum(livro.disponivel for livro in Livro.objects.all()),
			'emprestimos_pendentes': Emprestimo.objects.filter(status=Emprestimo.Status.PENDENTE).count(),
		})
		return context


class EmprestimoListView(ListView):
	model = Emprestimo
	template_name = 'emprestimos/lista.html'
	context_object_name = 'emprestimos'
	queryset = Emprestimo.objects.select_related('usuario', 'livro')


class EmprestimoCreateView(CreateView):
	form_class = EmprestimoForm
	template_name = 'formulario.html'
	success_url = reverse_lazy('emprestimos:lista')
	extra_context = {'titulo': 'Registrar empréstimo'}


class EmprestimoStatusUpdateView(UpdateView):
	model = Emprestimo
	form_class = StatusEmprestimoForm
	template_name = 'formulario.html'
	success_url = reverse_lazy('emprestimos:lista')
	extra_context = {'titulo': 'Atualizar status do empréstimo'}
