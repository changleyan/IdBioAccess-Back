# -*- coding: utf-8 -*-
from django.contrib.auth.models import Permission
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, JSONParser

from features.core.permissions.PermisoPermissions import PermisoPermissions
from features.core.serializers.PermisoSerializer import PermisoSerializer
from rest_framework.pagination import LimitOffsetPagination


class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = (PermisoPermissions,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    parser_classes = (MultiPartParser, JSONParser)
    pagination_class = LimitOffsetPagination  # Configura la paginación
