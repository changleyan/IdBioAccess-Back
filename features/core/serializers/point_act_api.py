from rest_framework import serializers
from features.core.models import *


class PointActSerializer(serializers.ModelSerializer):
    """
    Serializer for PointAct
    """
    class Meta:
        model = PointAct
        fields = '__all__'
