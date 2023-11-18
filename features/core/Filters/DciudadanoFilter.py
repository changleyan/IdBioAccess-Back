import django_filters

from features.core.models import Dciudadano


class DciudadanoFilter(django_filters.FilterSet):
    class Meta:
        model = Dciudadano
        fields = {
            'area': ['exact', 'icontains'],
            'roluniversitario': ['exact', 'icontains'],
            'primernombre': ['exact', 'icontains'],
            'segundonombre': ['exact', 'icontains'],
            'primerapellido': ['exact', 'icontains'],
            'segundoapellido': ['exact', 'icontains'],
            'solapin': ['exact', 'icontains'],
            'carnetidentidad': ['exact', 'icontains'],
            'provincia': ['exact', 'icontains'],
            'municipio': ['exact', 'icontains'],
            'sexo': ['exact', 'icontains'],
            'residente': ['exact'],
            'fechanacimiento': ['exact', 'gte', 'lte'],
            'idexpediente': ['exact', 'icontains'],
            'fecha': ['exact', 'gte', 'lte'],
            'idpersona': ['exact'],
        }
