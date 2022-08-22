from re import L
from django.contrib import admin
from tarjetas.models import Cards
from clientes.models import Cliente
from cuentas.models import Cuenta
from prestamos.models import Prestamo
from webitbank.models import (Empleado, Sucursal, Direcciones)
from movimiento.models import Movimientos


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ['card_id', 'numero_tarjeta', 'marca_tarjeta']
    pass



@admin.register(Cliente)    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_name', 
                    'customer_surname']
    pass



@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ['account_id', 'tipo_cuenta']
    pass


@admin.register(Direcciones)
class DireccionesAdmin(admin.ModelAdmin):
    list_display = ['calle', 'ciudad', 'provincia', 'pais']
    pass



@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee_name', 
                    'employee_surname', 'branch_id']
    pass

@admin.register(Movimientos)
class MovimientosAdmin(admin.ModelAdmin):
    list_display = ['movimiento_id', 'monto', 'fecha']
    pass


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['loan_id', 'loan_type', 'loan_date', 'account_id']
    pass



@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['branch_id', 'branch_name', 'branch_number']
    pass

