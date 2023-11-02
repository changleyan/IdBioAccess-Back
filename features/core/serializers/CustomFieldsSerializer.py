from rest_framework import serializers


class PermissionFieldSerializer(serializers.Field):

    def to_representation(self, obj):
        list_perms = []

        for perm in obj.all():
            list_perms.append(dict(
                id=perm.id,
                name=perm.name,
                codename=perm.codename
            ))
        return list_perms

    def to_internal_value(self, value):
        data = []
        if not isinstance(value, list):
            lista_ids = str(value).split(',')
            for id in lista_ids:
                id = id.strip()
                if id.isdigit():
                    data.append(int(id))
        else:
            data = value
        return data


class GruposFieldSerializer(serializers.Field):

    def to_representation(self, obj):
        data = []
        for group in obj.instance.groups.all():
            data.append(dict(
                id=group.id,
                name=group.name
            ))

        return data

    def to_internal_value(self, data):
        lista_palabras = []
        if not (not data):
            lista_id = data.split(',')
            for palabra in lista_id:
                palabra = palabra.strip()
                if palabra.isdigit():
                    lista_palabras.append(int(palabra))
        return lista_palabras