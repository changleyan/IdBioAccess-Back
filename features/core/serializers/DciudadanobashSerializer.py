from rest_framework import serializers

from features.core.models import Dciudadanobash


class DciudadanobashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dciudadanobash
        fields = '__all__'
