# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group
from rest_framework import serializers

from features.core.serializers.CustomFieldsSerializer import PermissionFieldSerializer


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionFieldSerializer()

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'permissions'
        ]
