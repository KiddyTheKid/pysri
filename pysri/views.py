from django.contrib.auth.models import User
from pysri.serializers import UserSerializer
from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
