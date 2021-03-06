from django.http import JsonResponse
from api.propuestas import services
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

def get_propuestas(request):
    lista_propuestas = services.obtener_propuestas()
    return JsonResponse(lista_propuestas)

def get_propuesta(request,id):
    if(request.method == "GET"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            propuesta = services.obtener_propuesta(id)
            return JsonResponse(propuesta)
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def get_propuestas_no_aprobadas(request):
    lista_propuestas = services.obtener_propuestas_no_aprobada()
    return JsonResponse(lista_propuestas)

def create_propuesta(request):
    if(request.method == "POST"):
        propuesta = json.loads(request.body)
        if( isEmpty(propuesta['titulo']) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.crear_propuesta(propuesta)
            return JsonResponse(successAction(200, 'Se creo exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def update_propuesta(request):
    if(request.method == "PUT"):
        data = json.loads(request.body)
        if( isEmpty(data['id']) or (not isNumber(data['id'])) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.actualizar_propuesta(data)
            return JsonResponse(successAction(200, 'Se actualizó el período exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def delete_propuesta(request, id):
    if(request.method == "DELETE"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.eliminar_propuesta(id)
            return JsonResponse(successAction(200, 'Se eliminó el período exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))