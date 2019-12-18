from django.shortcuts import render
from django.http import JsonResponse
from api.terms import services
from api.services.utils import isEmpty, generateError, successAction

# Create your views here.

def get_terms(request):
    lista_terms = services.obtener_terms()
    return JsonResponse(lista_terms)

def create_terms(request):
    print('llegueeeeee', request)
    if(isEmpty(request.term)):
        return JsonResponse(generateError(400, 'Ingrese un TERM valido.'))
    else: 
        services.crear_term()
        return JsonResponse(successAction(200, 'Se creo exitosamente'))