from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from features.core.models import *
from features.core.serializers.CustomFieldsSerializer import GruposFieldSerializer, PermissionFieldSerializer

username_validator = UnicodeUsernameValidator()
unique_validator = UniqueValidator(queryset=User.objects.all(), message='Este campo debe ser único.')

class AuthUserSerializer(serializers.ModelSerializer):
    """
    Serializer for Auth
    """
    groups = GruposFieldSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_active', 'email', 'ci', 'groups')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User
    """
    groups = GruposFieldSerializer()
    user_permissions = PermissionFieldSerializer()
    email = serializers.EmailField(max_length=50, required=False, validators=[unique_validator])
    username = serializers.CharField(validators=[unique_validator, username_validator])

    def get_fields(self, *args, **kwargs):
        fields = super(UserSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        view = self.context.get('view', None)

        if view and view.action in ['update', 'partial_update']:
            del fields['password']

        fields['email'].required = False
        fields['first_name'].required = False
        fields['last_name'].required = False
        fields['is_superuser'].required = False
        fields['is_staff'].required = False
        fields['groups'].required = False
        fields['user_permissions'].required = False
        fields['ci'].required = False
        fields['username'].required = True

        user = None
        if request:
            user = request.user

        if user and user.is_authenticated and not user.is_superuser:
            fields['is_superuser'].read_only = True
            fields['is_staff'].read_only = True

        return fields

    class Meta:
        model = User
        fields = '__all__'

        read_only_fields = (
            'date_joined',
            'last_login',
            'is_active',
        )

        extra_kwargs = {
            'password': {'write_only': True}
        }
        depth = 1

    @atomic
    def save(self, **kwargs):
        user = super(UserSerializer, self).save(**kwargs)
        if 'password' in self.initial_data.keys():
            user.set_password(self.initial_data['password'])
            user.save()
        return user
