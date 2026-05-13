from rest_framework import serializers
from productos.models import Producto


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = [
            "uuid",
            "codigo",
            "descripcion",
            "precio_unitario",
            "tiene_iva",
            "descripcion_adicional",
        ]
