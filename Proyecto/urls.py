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
from django.urls import path
from django.conf.urls import url
from api import views
from api.terms import urls as terms
from api.terms import views as views_terms
from api.usuarios import views as views_usuarios
from api.propuestas import views as views_propuestas
from api.trabajosdegrado import views as views_trabajosdegrado
from api.defensas import views as views_defensas

urlpatterns = [
    path('admin/', admin.site.urls),
    url('terms/', views_terms.get_terms),
    url('crear_term/', views_terms.create_terms),
    url('actualizar_term/', views_terms.update_term),
    path('eliminar_term/<int:id>/', views_terms.delete_term),
    url('usuarios/', views_usuarios.get_usuarios),
    path('usuario/<int:id>/', views_usuarios.get_usuario),
    url('crear_usuario/', views_usuarios.create_usuario),
    url('actualizar_usuario/', views_usuarios.update_usuario),
    path('eliminar_usuario/<int:id>/', views_usuarios.delete_usuario),
    url('propuestas/', views_propuestas.get_propuestas),
    path('propuesta/<int:id>/', views_propuestas.get_propuesta),
    url('crear_propuesta/', views_propuestas.create_propuesta),
    url('actualizar_propuesta/', views_propuestas.update_propuesta),
    path('eliminar_propuesta/<int:id>/', views_propuestas.delete_propuesta),
    url('trabajosdegrado/', views_trabajosdegrado.get_trabajosdegrado),
    path('trabajodegrado/<int:id>/', views_trabajosdegrado.get_trabajodegrado),
    url('crear_trabajodegrado/', views_trabajosdegrado.create_trabajodegrado),
    url('actualizar_trabajodegrado/', views_trabajosdegrado.update_trabajodegrado),
    path('eliminar_trabajodegrado/<int:id>/', views_trabajosdegrado.delete_trabajodegrado),
    url('defensas/', views_defensas.get_defensas),
    path('defensa/<int:id>/', views_trabajosdegrado.get_trabajodegrado),
    url('crear_defensa/', views_defensas.create_defensa),
    url('actualizar_defensa/', views_trabajosdegrado.update_trabajodegrado),
    path('eliminar_defensa/<int:id>/', views_trabajosdegrado.delete_trabajodegrado),
]
