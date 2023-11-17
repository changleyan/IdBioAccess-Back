# -*- coding: utf-8 -*-
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, JSONParser

from features.core.models import Nestado
from features.core.permissions.NestadoPermissions import NestadoPermissions
from features.core.serializers.NestadoSerializer import NestadoSerializer


class NestadoViewSet(viewsets.ModelViewSet):
    queryset = Nestado.objects.using('enrrolamiento').all()
    serializer_class = NestadoSerializer
    permission_classes = (NestadoPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
