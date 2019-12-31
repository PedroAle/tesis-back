from django.contrib import admin
from django.urls import path
from api.defensas import views as views_defensas

app_name = 'defensas'

urlpatterns = [
    path('', views_defensas.get_defensas),
    path('<int:id>/', views_defensas.get_defensa),
    path('crear/', views_defensas.create_defensa),
    path('actualizar/', views_defensas.update_defensa),
    path('eliminar/<int:id>/', views_defensas.delete_defensa),
]