from django.shortcuts import render
from django.http import JsonResponse
from api.services import terms, usuarios

# Create your views here.

"CRUD de TERM"

def get_terms(request):
    lista_terms = terms.obtener_terms()
    return JsonResponse(lista_terms)

def create_terms(request):
    response = terms.crear_terms()


"CRUD de USUARIO"

def get_usuarios(request):
    lista_usuarios = usuarios.obtener_usuarios()
    return JsonResponse(lista_usuarios)