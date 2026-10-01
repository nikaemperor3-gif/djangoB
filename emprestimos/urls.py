from django.urls import path
from .views import EmprestimoCreateView, EmprestimoListView, EmprestimoStatusUpdateView

app_name = 'emprestimos'

urlpatterns = [
    path('', EmprestimoListView.as_view(), name='lista'),
    path('novo/', EmprestimoCreateView.as_view(), name='novo'),
    path('<int:pk>/status/', EmprestimoStatusUpdateView.as_view(), name='status'),
]