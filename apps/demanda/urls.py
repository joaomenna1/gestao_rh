from django.urls import path
from .views import (DemandaList,
                    DemandaCreate,
                    DemandaUpdate,
                    DemandaDelete,

)
from .views import pdf_reportlab

urlpatterns = [
    path('list', DemandaList.as_view(), name='list_demanda'),
    path('novo', DemandaCreate.as_view(), name='create_demanda'),
    path('update/<int:pk>/', DemandaUpdate.as_view(), name='update_demanda'),
    path('delete/<int:pk>/', DemandaDelete.as_view(), name='delete_demanda'),
    path('pdf_reportlab', pdf_reportlab, name='pdf_reportlab'),

]
