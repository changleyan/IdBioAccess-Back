from rest_framework import permissions


class PermisoPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        return False

    def has_object_permission(self, request, view, application):
        if view.action in ['list']:
            return True
        return False