from django.db import models
from clientes.models import Cliente

# Create your models here.

"""21/08/22 Terminado"""
class TipoCuenta(models.Model):
    """Nos dice si la cuenta es ahorro en dolares, o ahorro en pesos, o cuenta corriente"""
    tipo_cuentaid = models.AutoField(db_column='tipo_cuentaId', primary_key=True)  # Field name made lowercase.
    
    
    tipo_cuenta = models.TextField()
    """Dolar, pesos, corriente"""
    class Meta:
        managed = True
        db_table = 'tipoCuenta'
    
    def __str__(self):
        return self.tipo_cuenta
        
        
class Cuenta(models.Model):
    account_id = models.IntegerField(primary_key=True, unique=True)
    customer_id = models.ForeignKey(Cliente, on_delete= models.CASCADE, to_field="customer_id", unique=True)
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete= models.CASCADE, to_field="tipo_cuentaid")

    class Meta:
        managed = True
        db_table = 'cuenta'

    def __str__(self):
        return str(f"{self.account_id}, {self.customer_id}, {self.tipo_cuenta}")