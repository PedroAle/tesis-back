from django.contrib import admin
from django.urls import path
from api.trabajosdegrado import views as views_trabajosdegrado

app_name = 'trabajosdegrado'

urlpatterns = [
    path('', views_trabajosdegrado.get_trabajosdegrado),
    path('<int:id>/', views_trabajosdegrado.get_trabajodegrado),
    path('crear/', views_trabajosdegrado.create_trabajodegrado),
    path('actualizar/', views_trabajosdegrado.update_trabajodegrado),
    path('eliminar/<int:id>/', views_trabajosdegrado.delete_trabajodegrado),
]