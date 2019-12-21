from django.http import JsonResponse
from api.terms import services
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

# Create your views here.

def get_correciones(request):
    lista_correciones = services.obtener_correciones()
    return JsonResponse(lista_correciones)

def create_terms(request):
    if(request.method == "POST"):
        term = json.loads(request.body)['term']
        if( isEmpty(term) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.crear_term(term)
            return JsonResponse(successAction(200, 'Se creo exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def update_term(request):
    if(request.method == "PUT"):
        data = json.loads(request.body)['data']
        if( isEmpty(data['id']) or isEmpty(data['term']) or (not isNumber(data['id'])) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.actualizar_term(data)
            return JsonResponse(successAction(200, 'Se actualizó el período exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def delete_term(request, id):
    if(request.method == "GET"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.eliminar_term(id)
            return JsonResponse(successAction(200, 'Se eliminó el período exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))