from django.contrib import admin
from django.urls import path
from api.usuarios import views as views_usuarios

app_name = 'usuarios'

urlpatterns = [
    path('', views_usuarios.get_usuarios),
    path('<int:id>/', views_usuarios.get_usuario),
    path('crear/', views_usuarios.create_usuario),
    path('actualizar/', views_usuarios.update_usuario),
    path('eliminar/<int:id>/', views_usuarios.delete_usuario),
    path('profesor/<int:id>/', views_usuarios.get_profesor_relacion),
]