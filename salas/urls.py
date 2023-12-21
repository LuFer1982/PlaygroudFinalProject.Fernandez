from django.urls import path
from salas.views import SalaAzulUpdate, SalaAzulDelete, SalaAzulLista, SalaAzulDetalle, SalaAmarillaUpdate, SalaAmarillaDelete, SalaAmarillaLista, SalaAmarillaDetalle, SalaRojaUpdate, SalaRojaDelete, SalaRojaLista, SalaRojaDetalle, SalaVerdeUpdate, SalaVerdeDelete, SalaVerdeLista, SalaVerdeDetalle, CrearNovedad
from . import views
from django import views
from .views import acerca_de_mi


#las definicion de las rutas para las vistas

urlpatterns = [
   path('editar_azul/<pk>/', SalaAzulUpdate.as_view(), name='editar_azul'),
   path('editar_roja/<pk>/', SalaRojaUpdate.as_view(), name='editar_roja'),
   path('editar_amarilla/<pk>/', SalaAmarillaUpdate.as_view(), name='editar_amarilla'),
   path('editar_verde/<pk>/', SalaVerdeUpdate.as_view(), name='editar_verde'),
   
   path('eliminar_azul/<pk>/', SalaAzulDelete.as_view(), name='eliminar_azul'),
   path('eliminar_roja/<pk>/', SalaRojaDelete.as_view(), name='eliminar_roja'),
   path('eliminar_amarilla/<pk>/', SalaAmarillaDelete.as_view(), name='eliminar_amarilla'),
   path('eliminar_verde/<pk>/', SalaVerdeDelete.as_view(), name='eliminar_verde'),
   
   path('<str:sala>/SalaAzulLista/', SalaAzulLista.as_view(), name='lista_azul'),
   path('<str:sala>/SalaRojaLista/', SalaRojaLista.as_view(), name='lista_roja'),
   path('<str:sala>/SalaAmarillaLista/', SalaAmarillaLista.as_view(), name='lista_amarilla'),
   path('<str:sala>/SalaVerdeLista/', SalaVerdeLista.as_view(), name='lista_verde'),
   
   path('SalaAzulLista/', SalaAzulLista.as_view(), name='lista_azul'),
   path('SalaRojaLista/', SalaRojaLista.as_view(), name='lista_roja'),
   path('SalaAmarillaLista/', SalaAmarillaLista.as_view(), name='lista_amarilla'),
   path('SalaVerdeLista/', SalaVerdeLista.as_view(), name='lista_verde'),

   path('<pk>/SalaAzulDetalle/', SalaAzulDetalle.as_view(), name='SalaAzulDetalle'),
   path('<pk>/SalaRojaDetalle/', SalaRojaDetalle.as_view(), name='SalaRojaDetalle'),
   path('<pk>/SalaAmarillaDetalle/', SalaAmarillaDetalle.as_view(), name='SalaAmarillaDetalle'),
   path('<pk>/SalaVerdeDetalle/', SalaVerdeDetalle.as_view(), name='SalaVerdeDetalle'),
   
   path('CrearNovedad/', CrearNovedad.as_view(), name= 'crear_novedad'),
   path('acerca_de_mi/', acerca_de_mi , name='acerca_de_mi'),
   
   ]