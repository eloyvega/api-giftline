from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Intercambio

User = get_user_model()


class IntercambioSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    tipo_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Intercambio
        fields = (
            'id', 'nombre', 'descripcion', 'status', 'status_display', 'tipo', 'tipo_display', 'fecha_creacion',
            'fecha_intercambio', 'links',
        )

    @staticmethod
    def get_status_display(obj):
        return obj.get_status_display()

    @staticmethod
    def get_tipo_display(obj):
        return obj.get_tipo_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('intercambio-detail', kwargs={'pk': obj.pk}, request=request),
        }


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links')

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request),
        }