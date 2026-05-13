from facturas.models import Factura
from facturas.serializers import FacturaSerializer
from rest_framework import permissions, viewsets


class FacturasViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [permissions.IsAuthenticated]
