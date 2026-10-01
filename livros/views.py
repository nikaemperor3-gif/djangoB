from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import LivroForm
from .models import Livro


class LivroListView(ListView):
	model = Livro
	template_name = 'livros/lista.html'
	context_object_name = 'livros'


class LivroCreateView(CreateView):
	form_class = LivroForm
	template_name = 'formulario.html'
	success_url = reverse_lazy('livros:lista')
	extra_context = {'titulo': 'Cadastrar livro'}
