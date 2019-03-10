from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtracreate,

)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horaExtra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_horaExtra'),
    path('delete/<int:pk>', HoraExtraDelete.as_view(), name='delete_horaExtra'),
    path('novo/', HoraExtracreate.as_view(), name='create_horaExtra'),


]
