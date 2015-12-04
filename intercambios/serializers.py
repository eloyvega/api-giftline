from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Intercambio

User = get_user_model()


class IntercambioSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    tipo_display = serializers.SerializerMethodField()

    class Meta:
        model = Intercambio
        fields = (
            'id', 'nombre', 'descripcion', 'status', 'status_display', 'tipo', 'tipo_display', 'fecha_creacion',
            'fecha_intercambio',
        )

    @staticmethod
    def get_status_display(obj):
        return obj.get_status_display()

    @staticmethod
    def get_tipo_display(obj):
        return obj.get_tipo_display()
