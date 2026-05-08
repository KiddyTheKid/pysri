from django.db import models
import uuid


class Empresa(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    ruc = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=250)
    nombre_comercial = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    direccion_matriz = models.CharField(max_length=250, null=True, blank=True)
    direccion_establecimiento = models.CharField(
        max_length=250, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=60, null=True, blank=True)
    codigo_establecimiento = models.CharField(max_length=3, default="001")
    punto_emision = models.CharField(max_length=3, default="001")
    tipo_ambiente = models.IntegerField(choices={
        1: "Produccion",
        2: "Pruebas",
    }, default=1)
    tipo_emision = models.IntegerField(choices={
        1: "Normal",
    }, default=1)
    obligado_contabilidad = models.BooleanField(default=False)
    contribuyente_especial = models.CharField(
        max_length=250, null=True, blank=True)
    email_notificacion = models.EmailField(
        max_length=60, null=True, blank=True)
    certificate = models.CharField(max_length=250, null=True, blank=True)
    certificate_password = models.CharField(max_length=250, null=True, blank=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
