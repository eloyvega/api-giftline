from django.conf import settings
from django.db import models


class Intercambio(models.Model):
    STATUS_ABIERTO = 1
    STATUS_CERRADO = 2
    STATUS_ELIMINADO = 3

    STATUS_OPCIONES = (
        (STATUS_ABIERTO, 'Abierto'),
        (STATUS_CERRADO, 'Cerrado'),
        (STATUS_ELIMINADO, 'Eliminado'),
    )

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    status = models.SmallIntegerField(choices=STATUS_OPCIONES, default=STATUS_ABIERTO)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_intercambio = models.DateField(blank=True, null=True)
    amigos = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Participante')

    def __str__(self):
        return self.nombre


class Participante(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    intercambio = models.ForeignKey(Intercambio)
    es_admin = models.BooleanField(default=False)
    amigo = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)


class Invitacion(models.Model):
    email_invitado = models.EmailField(max_length=254)
    intercambio = models.ForeignKey(Intercambio)
    mensaje = models.TextField(blank=True)
