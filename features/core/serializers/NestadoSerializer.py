from rest_framework import serializers

from features.core.models import Nestado


class NestadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nestado
        fields = '__all__'
