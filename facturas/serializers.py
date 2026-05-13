from rest_framework import serializers
from facturas.models import Factura


class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = "__all__"
