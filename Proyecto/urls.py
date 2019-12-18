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

urlpatterns = [
    path('admin/', admin.site.urls),
    url('terms/', views_terms.get_terms),
    url('crear_term/', views_terms.create_terms),
    url('actualizar_term/', views_terms.update_term),
    path('eliminar_term/<int:id>/', views_terms.delete_term),
    url('usuarios/', views_usuarios.get_usuarios),
    url('crear_usuario/', views_usuarios.create_usuario),
    url('actualizar_usuario/', views_usuarios.update_usuario),
    path('eliminar_usuario/<int:id>/', views_usuarios.delete_usuario),
]

""" url('crear_term/', view.create_term), """
""" url('usuarios/', views.get_usuarios) """
""" url('terms/', views.get_terms), """