from pyexpat import model
from django.db import models


class Direcciones(models.Model):
    
    direccion_id = models.AutoField(primary_key=True, unique=True, verbose_name='ID Direccion')
    calle = models.CharField(max_length = 255, blank=True, null=True, verbose_name = '')
    numero = models.IntegerField(blank=True, null=True, verbose_name = '')
    ciudad = models.CharField(max_length = 255, blank=True, null=True, verbose_name = '')
    pais = models.CharField(max_length = 255, blank=True, null=True, verbose_name = '')
    provincia = models.CharField(max_length = 255, blank=True, null=True, verbose_name = '')

    class Meta:
        managed = True
        db_table = 'direcciones'
        verbose_name = 'direccion'
        verbose_name_plural = 'direcciones'
        
    def __str__(self):
        return str(f"ID: {self.direccion_id}, CIUDAD: {self.ciudad}")


class Sucursal(models.Model):

    branch_id = models.AutoField(primary_key=True, unique=True, verbose_name = '')
    branch_number = models.IntegerField(verbose_name = '')
    branch_name = models.TextField(verbose_name = '')
    branch_address_id = models.IntegerField(verbose_name = '')
    direccion_id = models.ForeignKey(Direcciones, on_delete= models.CASCADE, to_field="direccion_id", verbose_name = '')
    class Meta:
        managed = True
        db_table = 'sucursal'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
    
    def __str__(self):
        return f"{self.branch_id}, {self.branch_name}"

class Empleado(models.Model):

    employee_id = models.AutoField(primary_key=True, verbose_name = '')
    employee_name = models.TextField(verbose_name = '')
    employee_surname = models.TextField(verbose_name = '')
    employee_hire_date = models.DateField(verbose_name = '')
    employee_dni = models.IntegerField(verbose_name = '')  # Field name made lowercase.
    branch_id = models.ForeignKey(Sucursal, on_delete= models.CASCADE, to_field="branch_id", verbose_name = '')
    direccion_id = models.ForeignKey(Direcciones, on_delete= models.CASCADE, to_field="direccion_id", verbose_name = '')

    class Meta:
        managed = True
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return f"{self.employee_name}, {self.employee_surname}"
