from django.db import models
import uuid


class Producto(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    codigo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    tiene_iva = models.BooleanField(default=True)
    descripcion_adicional = models.CharField(max_length=250, null=True, blank=True)
