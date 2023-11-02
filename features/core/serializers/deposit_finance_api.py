from rest_framework import serializers
from features.core.models import *


class DepositFinanceSerializer(serializers.ModelSerializer):
    """
    Serializer for DepositFinance
    """
    union_section_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = DepositFinance
        fields = '__all__'
        depth = 1
