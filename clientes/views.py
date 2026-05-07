from clientes.models import Clientes
from clientes.serializers import ClientesSerializer
from rest_framework import permissions, viewsets


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    permission_classes = [permissions.IsAuthenticated]