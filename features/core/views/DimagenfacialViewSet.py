# -*- coding: utf-8 -*-
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, JSONParser

from features.core.models import Dimagenfacial
from features.core.permissions.DimagenfacialPermissions import DimagenfacialPermissions
from features.core.serializers.DimagenfacialSerializer import DimagenfacialSerializer


class DimagenfacialViewSet(viewsets.ModelViewSet):
    queryset = Dimagenfacial.objects.using('enrrolamiento').all()
    serializer_class = DimagenfacialSerializer
    permission_classes = (DimagenfacialPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
