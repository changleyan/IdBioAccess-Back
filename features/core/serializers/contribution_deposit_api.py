from rest_framework import serializers
from features.core.models import *


class ContributionDepositSerializer(serializers.ModelSerializer):
    """
    Serializer for ContributionDeposit
    """
    union_section_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ContributionDeposit
        fields = '__all__'
        depth = 1
