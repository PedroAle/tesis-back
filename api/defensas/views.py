from django.http import JsonResponse
from api.defensas import services
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

# Create your views here.

def get_defensas(request):
    lista_defensas = services.obtener_defensas()
    return JsonResponse(lista_defensas)

def get_defensa(request,id):
    if(request.method == "GET"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            defensa = services.obtener_defensa(id)
            return JsonResponse(defensa)
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def create_defensa(request):
    if(request.method == "POST"):
        defensa = json.loads(request.body)
        if( isEmpty(defensa['codigo']) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.crear_defensa(defensa)
            return JsonResponse(successAction(200, 'Se creo exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def update_defensa(request):
    if(request.method == "PUT"):
        data = json.loads(request.body)
        if( isEmpty(data['id']) or (not isNumber(data['id'])) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.actualizar_defensa(data)
            return JsonResponse(successAction(200, 'Se actualizó el período exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def delete_defensa(request, id):
    if(request.method == "GET"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.eliminar_defensa(id)
            return JsonResponse(successAction(200, 'Se eliminó la defensa exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))