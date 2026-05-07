from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from rest_framework import permissions, viewsets


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
