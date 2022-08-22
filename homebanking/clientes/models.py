from django.db import models
from webitbank.models import Direcciones
from webitbank.models import Sucursal
from django.conf import settings
from .choices import tipo_cliente as tipo__
# Create your models here.
"""22/08/22 REVISADO"""

class Cliente(models.Model):
    
    customer_id = models.AutoField(primary_key=True, unique=True, verbose_name="Cliente ID")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                                     blank = False, null = False, verbose_name= "Usuario registrado")
    customer_name = models.CharField(max_length = 40, verbose_name= "Nombre")
    customer_surname = models.CharField(max_length = 40, verbose_name= "Apellido")  
    customer_dni = models.IntegerField(verbose_name= "DNI") 
    dob = models.DateField(blank=True, null=True, verbose_name= "Dob")
    
    branch = models.ForeignKey(Sucursal, on_delete = models.CASCADE,
                                  blank=False, null = False,
                                  to_field="branch_id", verbose_name= "Sucursal ID")
    
    tipo = models.CharField(max_length = 10, choices = tipo__, verbose_name= "Tipo de cliente")
    
    direccion = models.ForeignKey(Direcciones, on_delete = models.CASCADE,
                                     blank = False, null = False,
                                     to_field="direccion_id", verbose_name="Direccion")
    
    class Meta:
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        
    def __str__(self):
        return str(f"{self.customer_surname}, {self.customer_name}")

