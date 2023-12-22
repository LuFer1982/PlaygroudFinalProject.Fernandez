from django.urls import path
from usuarios.views import registro, login_request, PerfilUsuarioCreateView, PerfilUsuarioUpdateView, perfil_usuario
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_request, name='login'),
    path('registro/', registro, name='registro'),
    path('crear_perfil/', PerfilUsuarioCreateView.as_view(), name='crear perfil'),
    path('<pk>/editar_perfil/', PerfilUsuarioUpdateView.as_view(), name='editar perfil'),
    path('perfil_usuario/', perfil_usuario, name='ver perfil'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    
]