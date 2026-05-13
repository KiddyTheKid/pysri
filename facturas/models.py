from django.db import models
import uuid


class Factura(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    empresa_emisora_id = models.ForeignKey("empresas.Empresa", on_delete=models.CASCADE)
    cliente_id = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(default=None)
    clave_acceso = models.CharField(max_length=250)
    secuencial = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=20)
    total_sin_impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2)
    total_con_impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    xml = models.TextField(null=True, blank=True)
    xml_firmado = models.TextField(null=True, blank=True)
    ride_pdf = models.BinaryField(null=True, blank=True)
    autorizacion_numero = models.CharField(max_length=250, null=True, blank=True)
    autorizacion_fecha = models.DateTimeField(default=None, null=True, blank=True)
    sri_estado = models.CharField(max_length=250, null=True, blank=True)
    sri_mensajes = models.JSONField(null=True, blank=True)
    sri_fecha_envio = models.DateTimeField(default=None, null=True, blank=True)
    sri_fecha_respuesta = models.DateTimeField(default=None, null=True, blank=True)
    datos_originales = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        if not self.secuencial:
            ultimo_reg = (
                Factura.objects.filter(empresa_emisora_id=self.empresa_emisora_id)
                .order_by("-secuencial")
                .first()
            )
            if ultimo_reg:
                self.secuencial = ultimo_reg.secuencial + 1
            else:
                self.secuencial = 1
        super(Factura, self).save(**kwargs)

    class Meta:
        unique_together = ("empresa_emisora_id", "secuencial")
