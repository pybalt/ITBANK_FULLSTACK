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

    pass



@admin.register(Cliente)    
class ClienteAdmin(admin.ModelAdmin):

    pass



@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    
    pass


@admin.register(Direcciones)
class DireccionesAdmin(admin.ModelAdmin):

    pass



@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):

    pass

@admin.register(Movimientos)
class MovimientosAdmin(admin.ModelAdmin):

    pass


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):

    pass



@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):

    pass

