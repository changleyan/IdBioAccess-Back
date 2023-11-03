# -*- coding: utf-8 -*-

from rest_framework import permissions
from features.core.utilss.utils import *


class UserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        usuario = request.user
        is_authenticated = usuario.is_authenticated
        if view.action == 'me':
            return is_authenticated

        if view.action in ['update', 'partial_update']:
            id = view.kwargs['pk']
            is_active = convertir_bool('is_active', request.POST.get('is_active'))
            if is_active is not None and is_active and usuario.id == int(id) and not (
                    has_permission(request, view) and is_authenticated):
                raise exceptions.ValidationError(detail='No tiene permisos para realizar acciones de activación')
            return ((usuario.id == int(id) and has_permission(request, view)) or pertenece_grupo(usuario,
                                                                                                 G_ADMINISTRADOR)) and is_authenticated
        elif view.action in ['retrieve']:
            id = view.kwargs['pk']
            is_user = True
            if id is not None:
                is_user = usuario.id == int(id)
            return (is_user and has_permission(request, view)) or pertenece_grupo(usuario, G_ADMINISTRADOR) and is_authenticated
        elif view.action in ['destroy']:
            return has_permission(request, view) and is_authenticated
        elif view.action in ['create']:
            return is_authenticated and (has_permission(request, view) or pertenece_grupo(usuario, G_ADMINISTRADOR))
        elif view.action in ['list']:
            if request.GET.get('token') is not None:
                return is_authenticated
            if (has_permission(request, view) or pertenece_grupo(usuario, G_ADMINISTRADOR)) and is_authenticated:
                return True
            else:
                return False
        return False

    def has_object_permission(self, request, view, obj):
        usuario = request.user
        is_authenticated = usuario.is_authenticated

        if view.action in ['set_password']:
            return obj == usuario and is_authenticated
        elif view.action in ['me']:
            return (obj.id == usuario.id) and is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy', 'create']:
            print('Ret')
            return is_authenticated and has_permission(request, view) and (obj.id == usuario.id or pertenece_grupo(usuario, G_ADMINISTRADOR))
        return False
