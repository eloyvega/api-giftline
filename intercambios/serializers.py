from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Intercambio, Invitacion


class IntercambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intercambio
        fields = ('id', 'nombre', 'descripcion', 'fecha_creacion', 'fecha_intercambio')
