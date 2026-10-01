from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import UsuarioForm
from .models import Usuario


class UsuarioListView(ListView):
	model = Usuario
	template_name = 'usuarios/lista.html'
	context_object_name = 'usuarios'


class UsuarioCreateView(CreateView):
	form_class = UsuarioForm
	template_name = 'formulario.html'
	success_url = reverse_lazy('usuarios:lista')
	extra_context = {'titulo': 'Cadastrar usuário'}
