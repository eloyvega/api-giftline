from django.conf import settings
from django.db import models


class Intercambio(models.Model):
    STATUS_ABIERTO = 1
    STATUS_CERRADO = 2
    STATUS_ELIMINADO = 3
    TIPO_PUBLICO = 1
    TIPO_PRIVADO = 2

    STATUS_OPCIONES = (
        (STATUS_ABIERTO, 'Abierto'),
        (STATUS_CERRADO, 'Cerrado'),
        (STATUS_ELIMINADO, 'Eliminado'),
    )
    TIPO_OPCIONES = (
        (TIPO_PUBLICO, 'Público'),
        (TIPO_PRIVADO, 'Privado'),
    )

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    status = models.SmallIntegerField(choices=STATUS_OPCIONES, default=STATUS_ABIERTO)
    tipo = models.SmallIntegerField(choices=TIPO_OPCIONES, default=TIPO_PRIVADO)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_intercambio = models.DateField(blank=True, null=True)
    amigos = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Participante',
        through_fields=('intercambio', 'usuario')
    )

    def __str__(self):
        return self.nombre


class Participante(models.Model):
    intercambio = models.ForeignKey(Intercambio)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    es_admin = models.BooleanField(default=False)
    amigo = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='amigo',
    )


class Invitacion(models.Model):
    intercambio = models.ForeignKey(Intercambio)
    email_invitado = models.EmailField(max_length=254)
    mensaje = models.TextField(blank=True)
