# -*- coding: utf-8 -*-
from django.utils.encoding import force_bytes
from rest_framework import viewsets, filters, status
from rest_framework.parsers import MultiPartParser, JSONParser
from django.db import transaction
from rest_framework.response import Response

from features.core.models import Dimagenfacial
from features.core.permissions.DimagenfacialPermissions import DimagenfacialPermissions
from features.core.serializers.DimagenfacialSerializer import DimagenfacialSerializer

from features.core.models import Dciudadano  # Asegúrate de importar el modelo Dciudadano



class DimagenfacialViewSet(viewsets.ModelViewSet):
    queryset = Dimagenfacial.objects.using('enrrolamiento').all()
    serializer_class = DimagenfacialSerializer
    permission_classes = (DimagenfacialPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # Obtén el idciudadano de la solicitud
        idciudadano_id = request.data.get('idciudadano')

        # Busca el objeto Dciudadano en la base de datos enrrolamiento
        dciudadano = Dciudadano.objects.using('enrrolamiento').get(pk=idciudadano_id)

        # Asegúrate de que el campo 'foto' esté en la solicitud como archivo binario
        foto = force_bytes(request.data.get('foto'))

        # Ahora puedes crear el objeto Dimagenfacial con el Dciudadano correcto
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Asigna el objeto Dciudadano antes de guardar
        dimagenfacial = serializer.save(idciudadano=dciudadano, foto=foto)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
