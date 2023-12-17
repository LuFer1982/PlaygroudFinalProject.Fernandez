from django.views.generic import ListView, DetailView, UpdateView #agregar despues del import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #deberia ser from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
#from django.contrib.auth.views import LoginView, PasswordChangeView
#from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User
#from django.contrib.auth import login
#from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Comentario
from .forms import FormularioComentario
# este de aca arriba deberia ser from .forms import EditarNovedad, Novedad, FormularioCambioPassword, FormularioEdicion, FormularioCrearNovedad, FormularioRegistroUsuario, FormularioComentario

    
    # COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('index')

    #def form_valid(self, form):
     #   form.instance.comentario_id = self.kwargs['pk']
      #  return super(ComentarioPagina, self).form_valid(form)
