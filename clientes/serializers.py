from rest_framework import serializers
from clientes.models import Clientes


class ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clientes
        fields = ['uuid', 'tipo_identificacion_id', 'identificacion',
                  'razon_social', 'direccion', 'telefono', 'correo']
