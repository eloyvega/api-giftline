from rest_framework import viewsets
from .models import Intercambio
from .serializers import IntercambioSerializer


class IntercambioViewSet(viewsets.ModelViewSet):
    queryset = Intercambio.objects.order_by('fecha_creacion')
    serializer_class = IntercambioSerializer
