from rest_framework import serializers
from clientes.models import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            "uuid",
            "tipo_identificacion_id",
            "identificacion",
            "razon_social",
            "direccion",
            "telefono",
            "correo",
        ]
