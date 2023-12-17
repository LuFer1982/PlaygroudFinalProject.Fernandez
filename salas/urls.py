from django.urls import path
from salas.views import SalaAzulUpdate, SalaAzulDelete, SalaAzulLista, SalaAzulDetalle, CrearNovedad

#las definicion de las rutas para las vistas

urlpatterns = [
   path('<pk>/editar/', SalaAzulUpdate.as_view(), name='editar_Novedad'),
   path('<pk>/eliminar/', SalaAzulDelete.as_view(), name='eliminar_Novedad'),
   path('<str:sala>/SalaAzulLista/', SalaAzulLista.as_view(), name='lista_Novedad'),
   path('<pk>/SalaAzulDetalle/', SalaAzulDetalle.as_view(), name='SalaAzulDetalle'),
   path('CrearNovedad/', CrearNovedad.as_view(), name= 'crear_novedad'),
   ]