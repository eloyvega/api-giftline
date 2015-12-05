from django.contrib.auth import get_user_model
from rest_framework import viewsets, authentication, permissions

from .models import Intercambio
from .serializers import IntercambioSerializer, UserSerializer

User = get_user_model()


class ConfigMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class IntercambioViewSet(ConfigMixin, viewsets.ModelViewSet):
    queryset = Intercambio.objects.order_by('fecha_creacion')
    serializer_class = IntercambioSerializer


class UserViewSet(ConfigMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
