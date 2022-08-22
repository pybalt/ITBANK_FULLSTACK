from django.db import models
from cuentas.models import Cuenta
from .choices import marca_tarjeta as marcas
# Create your models here.
"""22/08/22 REVISADO"""


class Cards(models.Model):
    
    card_id = models.AutoField(primary_key=True, verbose_name="ID Tarjeta")
    
    account_id = models.ForeignKey(Cuenta, null=True, blank=True,
                                    on_delete=models.CASCADE, to_field="account_id", verbose_name="ID Cuenta")
    
    numero_tarjeta = models.IntegerField(verbose_name = "Numero de Tarjeta")  # This field type is a guess.
    
    cvv = models.IntegerField(verbose_name = "CVV")  # This field type is a guess.
    
    fecha_otorgamiento = models.DateField(verbose_name = "Fecha de otorgamiento", auto_now_add=True)  # This field type is a guess.
    
    fecha_expiracion = models.DateField(verbose_name = "Fecha de expiracion")  # This field type is a guess.
    
    marca_tarjeta = models.CharField(max_length=25, choices = marcas, verbose_name = "Tarjeta")  # Field name made lowercase. This field type is a guess.
    
    class Meta:
        managed = True
        db_table = 'cards'
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'
