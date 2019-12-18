""" from tastypie.resources import ModelResource
from api.models import Usuario

class UsuarioResource(ModelResource):
    class Meta:
        queryset = Usuario.objects.all()
        resource_name = 'usuario' """