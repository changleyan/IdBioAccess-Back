from rest_framework import serializers
from features.core.models import *


class AffiliateSerializer(serializers.ModelSerializer):
    """
    Serializer for Affiliate
    """
    initial_state_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Affiliate
        fields = '__all__'
        depth = 1
