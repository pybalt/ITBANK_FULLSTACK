from re import L
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from webitbank.models import (Usuario, Cards, Cliente,
                              Cuenta,
                              Empleado, Prestamo, Sucursal)


class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'usuario'

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


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



@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ['branch_id']
    list_display = ('employee_id', 'employee_name', 'employee_surname', 'branch_id')
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

