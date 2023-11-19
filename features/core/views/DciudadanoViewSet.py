# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response

from features.core.Filters.DciudadanoFilter import DciudadanoFilter
from features.core.models import Dciudadano, Dimagenfacial
from features.core.permissions.DciudadanoPermissions import DciudadanoPermissions
from features.core.serializers.DciudadanoSerializer import DciudadanoSerializer
from features.core.serializers.DimagenfacialSerializer import DimagenfacialSerializer


class DciudadanoViewSet(viewsets.ModelViewSet):
    queryset = Dciudadano.objects.using('enrrolamiento').all()
    serializer_class = DciudadanoSerializer
    permission_classes = (DciudadanoPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = DciudadanoFilter  # Usa tu clase de filtro personalizado aquí si es necesario
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        ciudadanos = []
        if page is not None:
            for ciudadano in page:
                imagen_facil_instance = Dimagenfacial.objects.filter(idciudadano=ciudadano).first()
                ciudadano_data = self.get_serializer(ciudadano).data
                imagen_facil_data = DimagenfacialSerializer(imagen_facil_instance).data if imagen_facil_instance else {}
                ciudadano_data['imagen_facil'] = imagen_facil_data
                ciudadanos.append(ciudadano_data)

            return self.get_paginated_response(ciudadanos)

        return Response(ciudadanos, status=status.HTTP_200_OK)
