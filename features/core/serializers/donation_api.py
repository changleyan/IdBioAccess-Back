from rest_framework import serializers
from features.core.models import *


class DonationSerializer(serializers.ModelSerializer):
    """
    Serializer for Donation
    """
    area_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Donation
        fields = '__all__'
        depth = 1
