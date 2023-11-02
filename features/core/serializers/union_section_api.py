from rest_framework import serializers
from features.core.models import *


class UnionSectionSerializer(serializers.ModelSerializer):
    """
    Serializer for UnionSection
    """
    area_id = serializers.IntegerField(write_only=True)
    initial_state_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = UnionSection
        fields = '__all__'
        #agregado lachy
        depth = 1
