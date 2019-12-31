from django.db import models
from django.utils.translation import gettext_lazy as _
from sqlite_orm.table import BaseTable

# Create your models here.
class Rol(models.Model):

    class TipoRol(models.TextChoices):
        ADMINISTRADOR = 'AD', _('Administrador')
        GESTOR = 'GT', _('Gestor')
        INVITADO = 'IN', _('Invitado')

    nombre_rol = models.CharField(
        max_length=2,
        choices=TipoRol.choices,
        default=TipoRol.INVITADO
    )

class Usuario(models.Model):

    class TipoUsuario(models.TextChoices):
        PROFESOR = 'PR', _('Profesor')
        ESTUDIANTE = 'ES', _('Estudiante')
        EXTERNO = 'EX', _('Externo')

    cedula = models.CharField(max_length=15)
    tipo = models.CharField(
        max_length=2,
        choices=TipoUsuario.choices,
        default=TipoUsuario.ESTUDIANTE,
    )
    primer_nombre = models.CharField(max_length=10)
    segundo_nombre = models.CharField(max_length=10, null=True)
    primer_apellido = models.CharField(max_length=10)
    segundo_apellido = models.CharField(max_length=10, null=True)
    correo_ucab = models.CharField(max_length=250, null=True)
    correo_personal = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    telefono_uno = models.CharField(max_length=11, null=True)
    telefono_dos = models.CharField(max_length=11, null=True)
    observaciones = models.TextField(null=True)
    fk_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Term(models.Model):
    term = models.CharField(max_length=6)

class Propuesta(models.Model):

    class Estatus(models.TextChoices):
        POREVALUAR = 'PE', _('Por Evaluar')
        DIFERIDA = 'DI', _('Diferida')
        APROBADA = 'AP', _('Aprobada')
        RECHAZADA = 'RE', _('Rechazada')

    codigo = models.CharField(max_length=50) #PREGUNTA: Codigo autoGenerado
    fecha_entrega = models.DateTimeField()
    titulo = models.CharField(max_length=250)
    estatus = models.CharField(
        max_length=2,
        choices=Estatus.choices,
        default=Estatus.POREVALUAR,
    )
    fk_term = models.ForeignKey(Term, on_delete=models.CASCADE)


class UsuarioPropuesta(models.Model):
    fk_propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE) 
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class TrabajoDeGrado(models.Model):

    class Estatus(models.TextChoices):
        PORENTREGAR = 'PE', _('Por Entregar')
        ENTREGADO = 'EP', _('Entregado y Pendiente por Defender')
        DIFERIDO = 'DI', _('Diferido')
        APROBADA = 'AP', _('Aprobada')
        APROBADAC = 'AC', _('Aprobada con Solicitud de Correciones')
        RECHAZADA = 'RE', _('Rechazada')

    codigo = models.CharField(max_length=250)
    titulo = models.CharField(max_length=250)
    nrc = models.CharField(max_length=50)
    descriptores = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    fecha_entrega = models.DateTimeField()
    nombre_empresa = models.CharField(max_length=100, null=True)
    estatus = models.CharField(
        max_length=2,
        choices=Estatus.choices,
        default=Estatus.PORENTREGAR,
    )
    fk_term = models.ForeignKey(Term, on_delete=models.CASCADE)
    fk_propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE)

class Defensa(models.Model):
    codigo = models.CharField(max_length=250)
    fecha_hora = models.DateTimeField()
    calificacion = models.DecimalField(max_digits=2, decimal_places=2)
    mencion_publicacion = models.BooleanField()
    mencion_honorifica = models.BooleanField()
    nota = models.BooleanField()
    fk_trabajo_grado = models.ForeignKey(TrabajoDeGrado, on_delete=models.CASCADE)

class Jurado(models.Model):
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_defensa = models.ForeignKey(Defensa, on_delete=models.CASCADE)
    suplente = models.BooleanField()

class Correcciones(models.Model):
    fecha = models.DateTimeField()
    fk_defensa = models.ForeignKey(Defensa, on_delete=models.CASCADE)