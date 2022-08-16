from django.db import models
from django.contrib.auth.models import User

class Cards(models.Model):
    customer_id = models.AutoField(primary_key=True)
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


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'



class Usuario(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_dni = models.ForeignKey(Cliente, on_delete=models.CASCADE)