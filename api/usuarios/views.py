from django.http import JsonResponse
from api.usuarios import services
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

# Create your views here.

def get_usuarios(request):
    lista_usuarios = services.obtener_usuarios()
    return JsonResponse(lista_usuarios)

def get_usuario(request,id):
    if(request.method == "GET"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            usuario = services.obtener_usuario(id)
            return JsonResponse(usuario)
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def get_profesor_relacion(request,id):
    if(request.method == "GET"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            usuario = services.obtener_relacionado_profesor(id)
            return JsonResponse(usuario)
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))


def create_usuario(request):
    if(request.method == "POST"):
        usuario = json.loads(request.body)
        if( isEmpty(usuario['cedula']) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.crear_usuario(usuario)
            return JsonResponse(successAction(200, 'Se creo el usuario exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def update_usuario(request):
    if(request.method == "PUT"):
        usuario = json.loads(request.body)
        print(usuario)
        if( isEmpty(usuario['id']) or isEmpty(usuario['cedula']) or (not isNumber(usuario['id'])) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.actualizar_usuario(usuario)
            return JsonResponse(successAction(200, 'Se actualizó el usuario exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))

def delete_usuario(request, id):
    if(request.method == "DELETE"):
        if( isEmpty(id) or (not isNumber(id)) ):
            return JsonResponse(generateError(400, 'Parámetros inválidos.'))
        else: 
            services.eliminar_usuario(id)
            return JsonResponse(successAction(200, 'Se eliminó el usuario exitosamente'))
    else:
        return JsonResponse(generateError(401, 'Método HTTP inválido'))