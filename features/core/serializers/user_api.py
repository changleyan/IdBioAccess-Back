from django.db.transaction import atomic
from rest_framework import serializers
from features.core.models import *


class AuthUserSerializer(serializers.ModelSerializer):
    """
    Serializer for Auth
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_active', 'email', 'ci')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User
    """
    password = serializers.CharField(write_only=True)
    union_section_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        depth = 1

    @atomic
    def save(self, **kwargs):
        user = super(UserSerializer, self).save(**kwargs)
        if 'password' in self.initial_data.keys():
            user.set_password(self.initial_data['password'])
            user.save()
        return user
