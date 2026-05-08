from productos.models import Producto
from productos.serializers import ProductoSerializer
from rest_framework import permissions, viewsets


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
