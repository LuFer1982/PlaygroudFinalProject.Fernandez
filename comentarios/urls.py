from django.urls import path
from salas.views import SalaAzulUpdate, SalaAzulDelete

#las definicion de las rutas para las vistas

urlpatterns = [
   path('SalaAzulUpdate/<titulo_Novedad>', SalaAzulUpdate.as_view(), name='editar_Novedad'),
   path('SalaAzulDelete/<titulo_Novedad>', SalaAzulDelete.as_view(), name='eliminar_Novedad'),
    ]