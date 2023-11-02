from rest_framework import serializers
from features.core.models import *


class AgreementSerializer(serializers.ModelSerializer):
    """
    Serializer for Agreement
    """
    act_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Agreement
        fields = '__all__'
        depth = 1
