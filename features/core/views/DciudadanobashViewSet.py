# -*- coding: utf-8 -*-
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, JSONParser

from features.core.models import Dciudadanobash
from features.core.permissions.DciudadanobashPermissions import DciudadanobashPermissions
from features.core.serializers.DciudadanobashSerializer import DciudadanobashSerializer


class DciudadanobashViewSet(viewsets.ModelViewSet):
    queryset = Dciudadanobash.objects.using('enrrolamiento').all()
    serializer_class = DciudadanobashSerializer
    permission_classes = (DciudadanobashPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
