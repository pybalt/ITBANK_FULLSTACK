from django.db import models
from webitbank.models import Direcciones
from webitbank.models import Sucursal
from django.conf import settings

# Create your models here.
"""21/08/22 Terminado"""

class TipoCliente(models.Model):
    "BLACK, GOLD, CLASSIC"
    tipo_clienteid = models.AutoField(primary_key=True, unique=True)  # Field name made lowercase.
    tipo_cliente = models.TextField()

    class Meta:
        managed = True
        verbose_name = 'Tipo de cliente'
        verbose_name_plural = 'Tipos de clientes'
        db_table = 'tipo_cliente'

    def __str__(self):
        return str(self.tipo_cliente)

class Cliente(models.Model):
    
    customer_id = models.IntegerField(primary_key=True, unique=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.IntegerField()  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.ForeignKey(Sucursal, on_delete = models.CASCADE, blank=False, null = False, to_field="branch_id")
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete = models.CASCADE, blank=False, null = False, to_field="tipo_clienteid")
    direccion_id = models.ForeignKey(Direcciones, on_delete = models.CASCADE, blank=False, null = False, to_field="direccion_id")
    class Meta:
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        
    def __str__(self):
        return str(f"{self.customer_surname}, {self.customer_name}")

