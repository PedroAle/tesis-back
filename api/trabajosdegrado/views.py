from django.http import JsonResponse
from api.trabajosdegrado import services
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

def get_trabajosdegrado(request):
    lista_trabajosdegrado = services.obtener_trabajosdegrado()
    return JsonResponse(lista_trabajosdegrado)

def get_trabajodegrado(request,id):
    if(request.method == "GET"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            trabajodegrado = services.obtener_trabajodegrado(id)
            return JsonResponse(trabajodegrado)
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def create_trabajodegrado(request):
    if(request.method == "POST"):
        trabajodegrado = json.loads(request.body)
        if( isEmpty(trabajodegrado['titulo']) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.crear_trabajodegrado(trabajodegrado)
            return JsonResponse(successAction(200, 'Se creo exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def update_trabajodegrado(request):
    if(request.method == "PUT"):
        data = json.loads(request.body)
        if( isEmpty(data['id']) or (not isNumber(data['id'])) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.actualizar_trabajodegrado(data)
            return JsonResponse(successAction(200, 'Se actualizó el período exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def delete_trabajodegrado(request, id):
    if(request.method == "DELETE"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.eliminar_trabajodegrado(id)
            return JsonResponse(successAction(200, 'Se eliminó el período exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))