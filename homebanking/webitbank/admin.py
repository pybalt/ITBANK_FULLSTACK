from re import L
from django.contrib import admin
from tarjetas.models import Cards
from clientes.models import (Cliente, TipoCliente)
from cuentas.models import (Cuenta, TipoCuenta)
from prestamos.models import Prestamo
from webitbank.models import (Empleado, Sucursal, Direcciones)
from movimiento.models import Movimientos


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    search_fields = ['marca_tarjetaid']
    list_display = ('numero_tarjeta', 'marca_tarjetaid')
    pass



@admin.register(Cliente)    
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['branch_id']
    list_display = ('customer_name', 'customer_surname', 'branch_id')
    pass



@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    search_fields = ['account_id']
    list_display = ('account_id', 'customer_id')
    pass


@admin.register(Direcciones)
class DireccionesAdmin(admin.ModelAdmin):
    list_display = ['direccion_id', 'ciudad', 'provincia', 'pais']
    search_fields = ('ciudad', )
    pass



@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ['branch_id']
    list_display = ('employee_id', 'employee_name', 'employee_surname', 'branch_id')
    pass

@admin.register(Movimientos)
class MovimientosAdmin(admin.ModelAdmin):
    list_display = ('movimiento_id', 'cuenta_remitente_id', 'cuenta_destinatario_id', 'monto')
    pass


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    search_fields = ['customer_id']
    list_display = ('loan_id', 'customer_id')
    pass



@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    search_fields = ['branch_id']
    list_display = ('branch_id', 'branch_name')
    pass

@admin.register(TipoCliente)
class TipoClienteAdmin(admin.ModelAdmin):
    list_display = ['tipo_cliente']
    pass

@admin.register(TipoCuenta)
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ['tipo_cuenta']
    pass
