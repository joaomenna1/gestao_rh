from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioNovo,
    Pdf,
    PdfDebug
)

from .views import relatorio_funcionarios


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('relatoriofuncionarios', relatorio_funcionarios, name='relatoriofuncionarios'),
    path('relatoriofuncionarios_html', Pdf.as_view(), name='relatoriofuncionarios_html'),
    path('relatoriofuncionarios_html_debug', PdfDebug.as_view(), name='relatoriofuncionarios_html_debug'),


]
