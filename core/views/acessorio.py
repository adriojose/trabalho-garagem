from rest_framework import viewsets
from core.models import Acessorio
from core.serializers import AcessorioSerializer


class AcessorioViewSet(viewsets.ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer