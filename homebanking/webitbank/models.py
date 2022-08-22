from pyexpat import model
from django.db import models

"""22/08/22 Revisado"""
class Direcciones(models.Model):
    
    direccion_id = models.AutoField(primary_key=True, unique=True, verbose_name='ID Direccion')
    calle = models.CharField(max_length = 50, blank=True, null=True, verbose_name = 'Calle')
    numero = models.IntegerField(blank=True, null=True, verbose_name = 'Numero')
    ciudad = models.CharField(max_length = 50, blank=True, null=True, verbose_name = 'Ciudad')
    pais = models.CharField(max_length = 50, blank=True, null=True, verbose_name = 'Pais')
    provincia = models.CharField(max_length = 50, blank=True, null=True, verbose_name = 'Provincia')

    class Meta:
        managed = True
        db_table = 'direcciones'
        verbose_name = 'direccion'
        verbose_name_plural = 'direcciones'
        
    def __str__(self):
        return str(f"ID: {self.direccion_id}, CIUDAD: {self.ciudad}")


class Sucursal(models.Model):

    branch_id = models.AutoField(primary_key= True, unique=True, verbose_name = 'ID Sucursal')
    branch_number = models.IntegerField(verbose_name = 'Numero de Sucursal')
    branch_name = models.CharField(max_length = 50, verbose_name = 'Nombre de Sucursal')
    branch_address = models.OneToOneField(Direcciones, on_delete= models.CASCADE, to_field="direccion_id", verbose_name = 'Direccion')
    class Meta:
        managed = True
        db_table = 'sucursal'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
    
    def __str__(self):
        return f"{self.branch_id}, {self.branch_name}"

class Empleado(models.Model):

    employee_id = models.AutoField(primary_key=True, verbose_name = 'ID Empleado')
    employee_name = models.CharField(max_length= 50, verbose_name = 'Nombre')
    employee_surname = models.CharField(max_length= 50, verbose_name = 'Apellido')
    employee_hire_date = models.DateField(verbose_name = 'Fecha de contratacion')
    employee_dni = models.IntegerField(verbose_name = 'DNI')
    branch = models.ForeignKey(Sucursal, on_delete= models.CASCADE, to_field="branch_id", verbose_name = 'Sucursal ID')
    direccion = models.ForeignKey(Direcciones, on_delete= models.CASCADE, to_field="direccion_id", verbose_name = 'Direccion ID')

    class Meta:
        managed = True
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return f"{self.employee_name}, {self.employee_surname}"
