from rest_framework.serializers import ModelSerializer, ValidationError
from empresas.models import Empresa


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        exclude = ["user_id"]
        read_only_fields = ["uuid"]
        write_only_fields = ["certificate_password"]

    def validate(self, data):
        print(data)
        certificate = data.get("certificate", None)
        certificate_password = data.get("certificate_password", None)
        print("Validandao", certificate_password)
        if certificate is None or certificate_password is None:
            raise ValidationError("Certificado y su contraseña son obligatorios")
        return data

    def create(self, validated_data):
        certificate = validated_data.pop("certificate", None)
        certificate_password = validated_data.pop("certificate_password", None)
        empresa = Empresa.objects.create(**validated_data)
        empresa.certificados.create(
            certificate=certificate, certificate_password=certificate_password
        )
        return empresa

    def update(self, instance, validated_data):
        certificate_password = validated_data.pop("certificate_password", None)
        instance = Empresa(**validated_data)
        certificado = instance.certificados.order_by("-created_at").first()
        if certificado and certificate_password is not None:
            certificado.certificate_password = certificate_password
            certificado.save()
        return instance
