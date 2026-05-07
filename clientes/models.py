from django.db import models
import uuid


class Cliente(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tipo_identificacion_id = models.CharField(choices={
        "04": "RUC",
        "05": "CÉDULA",
        "06": "PASAPORTE",
        "07": "VENTA AL CONSUMIDOR FINAL",
        "08": "IDENTIFICACION DEL EXTERIOR",
    }, default="05", max_length=2)
    identificacion = models.CharField(max_length=13, default="9999999999")
    razon_social = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)
