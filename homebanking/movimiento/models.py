from django.db import models
from cuentas.models import Cuenta
# Create your models here.

"""21/08/22 TERMINADO"""


class Movimientos(models.Model):
    
    movimiento_id = models.AutoField(primary_key=True)
    cuenta_remitente_id = models.ForeignKey(Cuenta, on_delete=models.CASCADE, blank=True, null=True, to_field='account_id', related_name="cuenta_remitente_id")
    cuenta_destinatario_id = models.ForeignKey(Cuenta, on_delete=models.CASCADE, blank=True, null=True, to_field='account_id', related_name="cuenta_destinatario_id")
    monto = models.IntegerField()
    tipo_movimiento = models.TextField()

    class Meta:
        managed = True
        db_table = 'movimientos'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        
    def __str__(self):
        return str(f"{self.movimiento_id}, {self.monto}")