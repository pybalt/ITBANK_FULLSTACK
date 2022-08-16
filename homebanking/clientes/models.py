from django.db import models

# Create your models here.

class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.TextField()

    class Meta:
        managed = False
        db_table = 'cliente'
"""
class TipoCliente(models.Model):
    tipo_clienteId = models.AutoField()
    tipo_cliente = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'
"""
