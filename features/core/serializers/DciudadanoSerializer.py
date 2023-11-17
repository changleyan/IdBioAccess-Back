from rest_framework import serializers

from features.core.models import Dciudadano


class DciudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dciudadano
        fields = '__all__'
