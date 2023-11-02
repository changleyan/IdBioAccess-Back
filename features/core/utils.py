from django.db import models
from rest_framework import serializers


class NullEmailField(models.EmailField):
    description = "EmailField which stores NULL and returns ''"

    def to_python(self, value, *args, **kwargs):
        if isinstance(value, models.CharField):
            return value
        return value or ''

    def get_db_prep_value(self, value, *args, **kwargs):
        return value or None


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordWithoutOldSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)