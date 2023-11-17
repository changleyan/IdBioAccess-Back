from rest_framework import serializers

from features.core.models import Dimagenfacial


class DimagenfacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimagenfacial
        fields = '__all__'
