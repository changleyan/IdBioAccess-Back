from rest_framework import serializers
from features.core.models import *


class ActSerializer(serializers.ModelSerializer):
    """
    Serializer for Act
    """
    union_section_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Act
        fields = '__all__'
        depth = 1
