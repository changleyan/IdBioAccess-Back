# -*- coding: utf-8 -*-
from rest_framework import permissions

from features.core.utilss.utils import has_permission


class NestadoPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        usuario = request.user
        is_authenticated = usuario.is_authenticated

        # los permisos 'create', 'partial_update', 'update', 'destroy' no estan aki pq los estados son de solo lectura
        if view.action in ['list', 'retrieve']:
            return has_permission(request, view) and is_authenticated
        return False

    def has_object_permission(self, request, view, application):
        usuario = request.user
        is_authenticated = usuario.is_authenticated

        if view.action in ['retrieve']:
            return has_permission(request, view) and is_authenticated
        return False
