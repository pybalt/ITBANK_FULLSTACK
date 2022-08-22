from django.db import models
from clientes.models import Cliente
from .choices import tipo_cuentas as tipo
# Create your models here.

"""22/08/22 REVISADO"""
import uuid

class Cuenta(models.Model):
     
    account_id = models.AutoField(primary_key = True, unique = True, verbose_name="ID Cuenta")
    
    customer = models.ForeignKey(Cliente, on_delete = models.CASCADE, to_field="customer_id", verbose_name="Cliente")
    
    balance = models.IntegerField(verbose_name="Balance")
    
    tipo_cuenta = models.CharField(max_length = 10, choices=tipo, verbose_name="Tipo de cuenta")

    iban = models.CharField(max_length = 10, editable = False, verbose_name = """IBAN. 
                            Dejar en Blanco para generar automaticamente""")

    
    def save(self, *args, **kwargs):
        iban = str(uuid.uuid4()).replace("-","")[:12]
        self.iban = iban
        super(Cuenta, self).save(*args, **kwargs)
    
    class Meta:
        managed = True
        db_table = 'cuenta'

    def __str__(self):
        return str(f"{self.account_id}, {self.customer}, {self.tipo_cuenta}")
    