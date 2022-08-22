from xml.dom import ValidationErr
from django.db import models
from cuentas.models import Cuenta
from .choices import tipo_movimientos as tipo
from django.core.exceptions import ValidationError
# Create your models here.

"""22/08/22 REVISADO"""


class Movimientos(models.Model):
    
    movimiento_id = models.AutoField(primary_key=True, verbose_name='ID Movimiento')
    cuenta_remitente_id = models.ForeignKey(Cuenta, on_delete = models.CASCADE, blank=False, null=False,
                                            to_field='account_id', related_name="cuenta_remitente_id",
                                            verbose_name='Remitente')
    cuenta_destinatario_id = models.ForeignKey(Cuenta, on_delete = models.CASCADE, blank=True, null=True,
                                               to_field='account_id', related_name="cuenta_destinatario_id",
                                               verbose_name='Destinatario')
    monto = models.IntegerField(verbose_name = 'Monto')
    tipo_movimiento = models.CharField(max_length = 10, choices = tipo, verbose_name = 'Tipo de Movimiento')

    def clean(self):
        if self.cuenta_destinatario_id == self.cuenta_remitente_id:
            raise ValidationError('El remitente y el destinatario son iguales')
    class Meta:
        managed = True
        db_table = 'movimientos'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        
    def __str__(self):
        return str(f"{self.movimiento_id}, {self.monto}")