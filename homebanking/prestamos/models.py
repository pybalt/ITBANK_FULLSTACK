from django.db import models
from clientes.models import Cliente
from cuentas.models import Cuenta
from .choices import tipo_prestamo
# Create your models here.
"""22/08/22"""


class Prestamo(models.Model):
    
    loan_id = models.AutoField(primary_key = True, verbose_name = "ID Prestamo")
    loan_type = models.CharField(choices=tipo_prestamo, max_length = 15, verbose_name = "Tipo de prestamo")
    loan_date = models.DateField(verbose_name = "Fecha del prestamo")
    loan_total = models.IntegerField(verbose_name = "Monto")
    account = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=False,
                                blank=False, verbose_name = "ID Cuenta")
    
    class Meta:
        managed = True
        db_table = 'prestamo'
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'