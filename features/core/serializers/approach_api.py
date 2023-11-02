from rest_framework import serializers
from features.core.models import *


class ApproachSerializer(serializers.ModelSerializer):
    """
    Serializer for Approach
    """
    act_id = serializers.IntegerField(write_only=True)
    affiliate_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Approach
        fields = '__all__'
        depth = 1
