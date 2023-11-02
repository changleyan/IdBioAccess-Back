from rest_framework import serializers
from features.core.models import *


class AreaSerializer(serializers.ModelSerializer):
    """
    Serializer for Area
    """
    class Meta:
        model = Area
        fields = '__all__'
