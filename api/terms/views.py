from django.shortcuts import render
from django.http import JsonResponse
from api.terms import services
from api.services.utils import isEmpty, generateError, successAction
import json

# Create your views here.

def get_terms(request):
    lista_terms = services.obtener_terms()
    return JsonResponse(lista_terms)

def create_terms(request):
    if(request.method == "POST"):
        term = json.loads(request.body)['term']
        if( isEmpty(term) ):
            return JsonResponse(generateError(400, 'Ingrese un TERM valido.'))
        else: 
            services.crear_term(term)
            return JsonResponse(successAction(200, 'Se creo exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))
    