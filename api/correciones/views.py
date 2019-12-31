from django.http import JsonResponse
from api.correciones import services
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

def get_correcciones(request):
    lista_correcciones = services.obtener_correcciones()
    return JsonResponse(lista_correcciones)

def create_correccion(request):
    if(request.method == "POST"):
        correccion = json.loads(request.body)
        if( isEmpty(correccion['defensa']) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.crear_correccion(correccion)
            return JsonResponse(successAction(200, 'Se creo exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def update_correccion(request):
    if(request.method == "PUT"):
        correccion = json.loads(request.body)
        if( isEmpty(correccion['id']) or isEmpty(correccion['fecha']) or (not isNumber(correccion['id'])) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.actualizar_correccion(correccion)
            return JsonResponse(successAction(200, 'Se actualizó la correccion exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def delete_correccion(request, id):
    if(request.method == "DELETE"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.eliminar_correccion(id)
            return JsonResponse(successAction(200, 'Se eliminó la correccion exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))