from django.contrib import admin
from django.urls import path
from api.terms import views

app_name = 'terms'

urlpatterns = [
    path('', views.get_terms),
    path('crear/', views.create_terms),
    path('actualizar/', views.update_term),
    path('eliminar/<int:id>/', views.delete_term)
]