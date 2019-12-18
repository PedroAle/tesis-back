from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from api.terms import views


app_name = 'terms'

urlpatterns = [
    url('get_all/', views.get_terms)
]