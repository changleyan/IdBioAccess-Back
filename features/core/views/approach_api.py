from rest_framework.viewsets import ModelViewSet
from features.core.serializers import *


class ApproachApiView(ModelViewSet):
    """
    View with all crud methods
    list | create | update | delete | details
    GET  |  POST  |  PATH  | DELETE | GET <id>
    """
    queryset = Approach.objects.all()
    serializer_class = ApproachSerializer

