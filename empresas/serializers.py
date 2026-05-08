from rest_framework.serializers import ModelSerializer
from empresas.models import Empresa


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        read_only_fields = ['uuid']
