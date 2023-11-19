import django_filters

from features.core.models import Dciudadano


class DciudadanoFilter(django_filters.FilterSet):
    solapin = django_filters.CharFilter(field_name='solapin', lookup_expr='icontains')
    carnetidentidad = django_filters.CharFilter(field_name='carnetidentidad', lookup_expr='icontains')
    primernombre = django_filters.CharFilter(field_name='primernombre', lookup_expr='icontains')
    segundonombre = django_filters.CharFilter(field_name='segundonombre', lookup_expr='icontains')
    area = django_filters.CharFilter(field_name='area', lookup_expr='icontains')
    roluniversitario = django_filters.CharFilter(field_name='roluniversitario', lookup_expr='icontains')

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
