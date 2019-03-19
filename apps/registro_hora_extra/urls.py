from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtracreate,
    UtilizouHoraExtra,
    ExportarParaCSV,
    ExportarExcel

)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horaExtra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_horaExtra'),
    path('delete/<int:pk>', HoraExtraDelete.as_view(), name='delete_horaExtra'),
    path('utilizou-hora-extra/<int:pk>',
         UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('novo/', HoraExtracreate.as_view(), name='create_horaExtra'),
    path('exportar/', ExportarParaCSV.as_view(), name='exportar_csv'),
    path('exportar-excel/', ExportarExcel.as_view(), name='exportar_excel'),


]
