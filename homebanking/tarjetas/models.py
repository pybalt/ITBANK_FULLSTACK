from django.db import models
from clientes.models import (Cliente, TipoCliente)
from cuentas.models import TipoCuenta

# Create your models here.
"""21/08/22 TERMINADO"""


class Cards(models.Model):
    card_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE, to_field="customer_id")
    numero_tarjeta = models.IntegerField()  # This field type is a guess.
    cvv = models.IntegerField()  # This field type is a guess.
    fecha_otorgamiento = models.DateField()  # This field type is a guess.
    fecha_expiracion = models.DateField()  # This field type is a guess.
    marca_tarjetaid = models.TextField()  # Field name made lowercase. This field type is a guess.
    tipo_clienteid = models.ForeignKey(TipoCliente, null=True, blank=True, on_delete=models.CASCADE, to_field="tipo_clienteid")  # Field name made lowercase. This field type is a guess.
    tipo_cuentaid = models.ForeignKey(TipoCuenta, null=True, blank=True, on_delete=models.CASCADE, to_field="tipo_cuentaid")  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'cards'
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'