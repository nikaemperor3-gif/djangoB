from django.urls import path
from .views import UsuarioCreateView, UsuarioListView

app_name = 'usuarios'

urlpatterns = [
    path('', UsuarioListView.as_view(), name='lista'),
    path('novo/', UsuarioCreateView.as_view(), name='novo'),
]