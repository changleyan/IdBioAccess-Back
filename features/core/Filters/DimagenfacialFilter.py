import django_filters

from features.core.models import Dimagenfacial


class DimagenfacialFilter(django_filters.FilterSet):
    class Meta:
        model = Dimagenfacial
        fields = {
            'idciudadano__area': ['exact', 'icontains'],
            'idciudadano__roluniversitario': ['exact', 'icontains'],
            'idciudadano__primernombre': ['exact', 'icontains'],
            'idciudadano__segundonombre': ['exact', 'icontains'],
            'idciudadano__primerapellido': ['exact', 'icontains'],
            'idciudadano__segundoapellido': ['exact', 'icontains'],
            'idciudadano__solapin': ['exact', 'icontains'],
            'idciudadano__carnetidentidad': ['exact', 'icontains'],
            'idciudadano__provincia': ['exact', 'icontains'],
            'idciudadano__municipio': ['exact', 'icontains'],
            'idciudadano__sexo': ['exact', 'icontains'],
            'idciudadano__residente': ['exact'],
            'idciudadano__fechanacimiento': ['exact', 'gte', 'lte'],
            'idciudadano__idexpediente': ['exact', 'icontains'],
            'idciudadano__fecha': ['exact', 'gte', 'lte'],
            'idciudadano__idpersona': ['exact'],
            'valida': ['exact'],
            'fecha': ['exact', 'gte', 'lte'],
            'fecha_actualizacion': ['exact', 'gte', 'lte'],
        }
