from django.views.generic import ListView, DetailView, UpdateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Novedad
from .forms import EditarNovedad, Novedad, FormularioCrearNovedad
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


# ACERCA DE MI
def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

# PERMISOS AL AUTOR O AL DOCENTE
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

def puede_editar_novedad(user, novedad):
    """
    Verifica si el usuario tiene permisos para editar la novedad.
    Permite la edición si el usuario es el autor o si tiene el rol de docente.
    """
    return user == novedad.usuario or user.rol == 'docente'


    

# SALA AZUL

class SalaAzulLista(LoginRequiredMixin, ListView): 
    model = Novedad
    context_object_name = 'sala_azul'
    template_name = 'listaAzul.html'
 
    def get_queryset(self):
        return Novedad.objects.filter(sala='azul')
  
class SalaAzulDetalle(LoginRequiredMixin, DetailView):
    model = Novedad
    template_name = 'azulDetalle.html'
    success_url = reverse_lazy ("lista_azul")
    
    def get_queryset(self): 
        return Novedad.objects.filter(usuario=self.request.user)

class SalaAzulUpdate(LoginRequiredMixin, UpdateView): 
    model = Novedad
    form_class = EditarNovedad
    success_url = reverse_lazy('lista_azul')
    template_name = 'azulEdicion.html'
   
    
   
class SalaAzulDelete(LoginRequiredMixin, DeleteView):
    model = Novedad
    success_url = reverse_lazy('lista_azul')
    template_name = 'azulBorrado.html'


# SALA ROJA

class SalaRojaLista(LoginRequiredMixin, ListView): 
    model = Novedad
    context_object_name = 'sala_roja'
    template_name = 'listaRoja.html'
    
    def get_queryset(self):
        return Novedad.objects.filter(sala='roja')
  
class SalaRojaDetalle(LoginRequiredMixin, DetailView):
    model = Novedad
    template_name = 'rojaDetalle.html'
    success_url = reverse_lazy ("lista_roja")
   

class SalaRojaUpdate(LoginRequiredMixin, UpdateView): 
    model = Novedad
    form_class = EditarNovedad
    success_url = reverse_lazy('lista_roja')
    template_name = 'rojaEdicion.html'
   
    def get_queryset(self):
        return Novedad.objects.filter(usuario=self.request.user)
    
class SalaRojaDelete(LoginRequiredMixin, DeleteView):
    model = Novedad
    success_url = reverse_lazy('lista_roja')
    template_name = 'rojaBorrado.html'


# SALA AMARILLA

class SalaAmarillaLista(LoginRequiredMixin, ListView): 
    model = Novedad
    context_object_name = 'sala_amarilla'
    template_name = 'listaAmarilla.html'

    def get_queryset(self):
        return Novedad.objects.filter(sala='amarilla')
  
class SalaAmarillaDetalle(LoginRequiredMixin, DetailView):
    model = Novedad
    template_name = 'amarillaDetalle.html'
    success_url = reverse_lazy ("lista_amarilla")
   

class SalaAmarillaUpdate(LoginRequiredMixin, UpdateView): 
    model = Novedad
    form_class = EditarNovedad
    success_url = reverse_lazy('lista_amarilla')
    template_name = 'amarillaEdicion.html'
    
    def get_queryset(self):
        return Novedad.objects.filter(usuario=self.request.user)
   
class SalaAmarillaDelete(LoginRequiredMixin, DeleteView):
    model = Novedad
    success_url = reverse_lazy('lista_amarilla')
    template_name = 'amarillaBorrado.html'
    
# SALA VERDE

class SalaVerdeLista(LoginRequiredMixin, ListView): 
    model = Novedad
    context_object_name = 'sala_verde'
    template_name = 'listaVerde.html'

    def get_queryset(self):
        return Novedad.objects.filter(sala='verde')
  
class SalaVerdeDetalle(LoginRequiredMixin, DetailView):
    model = Novedad
    template_name = 'verdeDetalle.html'
    success_url = reverse_lazy ("lista_verde")
   

class SalaVerdeUpdate(LoginRequiredMixin, UpdateView): 
    model = Novedad
    form_class = EditarNovedad
    success_url = reverse_lazy('lista_verde')
    template_name = 'verdeEdicion.html'
   
    def get_queryset(self):
        return Novedad.objects.filter(usuario=self.request.user)
   
class SalaVerdeDelete(LoginRequiredMixin, DeleteView):
    model = Novedad
    success_url = reverse_lazy('lista_verde')
    template_name = 'verdeBorrado.html'


    # CREACION NOVEDAD

class CrearNovedad (LoginRequiredMixin, CreateView): 
    model = Novedad
    form_class = FormularioCrearNovedad
    template_name = 'novedadCreacion.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.sala = form.cleaned_data['sala'] 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('principal')
    





    
   