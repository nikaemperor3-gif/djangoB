from django.urls import path
from .views import LivroCreateView, LivroListView

app_name = 'livros'

urlpatterns = [
    path('', LivroListView.as_view(), name='lista'),
    path('novo/', LivroCreateView.as_view(), name='novo'),
]