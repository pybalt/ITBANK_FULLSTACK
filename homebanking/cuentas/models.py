from django.db import models

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'

class Tipocuenta(models.Model):
    tipo_cuentaid = models.AutoField(db_column='tipo_cuentaId', primary_key=True)  # Field name made lowercase.
    tipo_cuenta = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipoCuenta'