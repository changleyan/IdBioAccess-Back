import base64

from rest_framework import serializers


from features.core.models import Dimagenfacial


class DimagenfacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimagenfacial
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(DimagenfacialSerializer, self).to_representation(instance)

        # Asegúrate de que 'foto' sea devuelto como una cadena base64
        if 'foto' in representation:
            # Obtén la imagen base64 de la base de datos
            imagen_base64 = representation['foto']

            # Convierte la cadena base64 a bytes
            imagen_bytes = base64.b64decode(imagen_base64)

            representation['foto'] = imagen_bytes

        return representation