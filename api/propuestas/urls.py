from django.contrib import admin
from django.urls import path
from api.propuestas import views as views_propuestas

app_name = 'propuestas'

urlpatterns = [
    path('', views_propuestas.get_propuestas),
    path('<int:id>/', views_propuestas.get_propuesta),
    path('crear/', views_propuestas.create_propuesta),
    path('actualizar/', views_propuestas.update_propuesta),
    path('eliminar/<int:id>/', views_propuestas.delete_propuesta)
]