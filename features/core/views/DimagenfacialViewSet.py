# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_bytes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.parsers import MultiPartParser, JSONParser
from django.db import transaction
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from features.core.Filters.DimagenfacialFilter import DimagenfacialFilter
from features.core.models import Dimagenfacial
from features.core.permissions.DimagenfacialPermissions import DimagenfacialPermissions
from features.core.serializers.DimagenfacialSerializer import DimagenfacialSerializer

from features.core.models import Dciudadano  # Asegúrate de importar el modelo Dciudadano



class DimagenfacialViewSet(ModelViewSet):
    queryset = Dimagenfacial.objects.using('enrrolamiento').all()
    serializer_class = DimagenfacialSerializer
    permission_classes = (DimagenfacialPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = DimagenfacialFilter  # Usa tu clase de filtro personalizado aquí si es necesario
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

        serializer.save(idciudadano=dciudadano, foto=foto)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        serializer = self.get_instance(request, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):
        serializer = self.get_instance(request, kwargs)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def get_instance(self, request, kwargs):
        pk = kwargs['pk']
        instance = get_object_or_404(self.queryset, pk=pk)
        self.check_object_permissions(request, instance)
        serializer = DimagenfacialSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Asegúrate de que el campo 'foto' esté en la solicitud como archivo binario
        foto = force_bytes(request.data.get('foto'))

        serializer.save(foto=foto)

        return Response(serializer.data)