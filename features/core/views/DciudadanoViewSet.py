# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, JSONParser

from features.core.Filters.DciudadanoFilter import DciudadanoFilter
from features.core.models import Dciudadano
from features.core.permissions.DciudadanoPermissions import DciudadanoPermissions
from features.core.serializers.DciudadanoSerializer import DciudadanoSerializer


class DciudadanoViewSet(viewsets.ModelViewSet):
    queryset = Dciudadano.objects.using('enrrolamiento').all()
    serializer_class = DciudadanoSerializer
    permission_classes = (DciudadanoPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = DciudadanoFilter  # Usa tu clase de filtro personalizado aquí si es necesario
    ordering_fields = '__all__'
