from django.db import models

# Create your models here.

class Cards(models.Model):
    customer_id = models.AutoField()
    numero_tarjeta = models.TextField()  # This field type is a guess.
    cvv = models.TextField()  # This field type is a guess.
    fecha_otorgamiento = models.TextField()  # This field type is a guess.
    fecha_expiracion = models.TextField()  # This field type is a guess.
    marca_tarjetaid = models.TextField(db_column='marca_tarjetaId')  # Field name made lowercase. This field type is a guess.
    tipo_clienteid = models.TextField(db_column='tipo_clienteId')  # Field name made lowercase. This field type is a guess.
    tipo_cuentaid = models.TextField(db_column='tipo_cuentaId')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cards'