"""
URL configuration for entregable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from cartelera.views import pag_principal
from django.conf import settings
from django.conf.urls.static import static

#la url de la app y de la pagina principal
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pag_principal, name="principal"),
    # URLs de apps:
    path('salas/', include('salas.urls')),
    path('comentarios/', include('comentarios.urls')),
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)