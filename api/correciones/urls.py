from django.contrib import admin
from django.urls import path
from api.correciones import views as views_correcciones

app_name = 'correciones'

urlpatterns = [
    path('', views_correcciones.get_correcciones),
    path('crear/', views_correcciones.create_correccion),
    path('actualizar/', views_correcciones.update_correccion),
    path('eliminar/<int:id>/', views_correcciones.delete_correccion)
]