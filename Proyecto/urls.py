"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from api.terms import urls as urls_terms
from api.usuarios import urls as urls_usuarios
from api.propuestas import urls as urls_propuestas
from api.trabajosdegrado import urls as urls_trabajosdegrado
from api.defensas import urls as urls_defensas
from api.correciones import urls as urls_correcciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('terms/', include(urls_terms)),
    path('usuarios/', include(urls_usuarios)),
    path('propuestas/', include(urls_propuestas)),
    path('tg/', include(urls_trabajosdegrado)),
    path('defensas/', include(urls_defensas)),
    path('correcciones/', include(urls_correcciones))
]
