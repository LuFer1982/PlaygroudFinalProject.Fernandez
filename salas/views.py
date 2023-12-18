from django.views.generic import ListView, DetailView, UpdateView, TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
#from django.contrib.auth.views import LoginView, PasswordChangeView
#from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User
#from django.contrib.auth import login
#from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Novedad
from django.shortcuts import get_object_or_404
from .forms import EditarNovedad, Novedad, FormularioCrearNovedad
# este de aca arriba deberia ser from .forms import EditarNovedad, Novedad, FormularioCambioPassword, FormularioEdicion, FormularioCrearNovedad, FormularioRegistroUsuario, FormularioComentario


# SALA AZUL

class SalaAzulLista (ListView): #class SalaAzulLista (LoginRequiredMixin, ListView):
    model = Novedad
    context_object_name = 'sala_azul'
    template_name = 'listaAzul.html'
    #login_url = '/login/'

  
class SalaAzulDetalle(DetailView): #class SalaAzulDetalle(LoginRequiredMixin, DetailView):
    model = Novedad
    template_name = 'azulDetalle.html'
    success_url = reverse_lazy ("lista_Novedad")
   

class SalaAzulUpdate(UpdateView): #class SalaAzulUpdate(LoginRequiredMixin, UpdateView):
    model = Novedad
    form_class = EditarNovedad
    success_url = reverse_lazy('lista_Novedad')
    #context_object_name = 'sala_azul'
    template_name = 'azulEdicion.html'
    
class SalaAzulDelete(DeleteView): #class SalaAzulDelete(LoginRequiredMixin, DeleteView):
    model = Novedad
    success_url = reverse_lazy('lista_Novedad')
    #context_object_name = 'sala azul'
    template_name = 'azulBorrado.html'
    
    # CREACION NOVEDAD

class CrearNovedad(CreateView): #class CrearNovedad (LoginRequiredMixin, CreateView):
    model = Novedad
    form_class = FormularioCrearNovedad
    template_name = 'novedadCreacion.html'
    
    def form_valid(self, form):
        form.instance.sala = 'sala'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lista_Novedad', kwargs={'sala': self.object.sala})

  
    
   