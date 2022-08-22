from rest_framework import serializers
"""Obtener tarjetas asociadas a un cliente"""
from clientes.models import Cliente
"""Modificar direccion de un cliente"""
from webitbank.models import Direcciones
from tarjetas.models import Cards, Cuenta
"""Anular solicitud de prestamo de un cliente"""
from prestamos.models import Prestamo
"""Listado de todas las sucursales"""
from webitbank.models import Sucursal

class TarjetasSerializer(serializers.ModelSerializer):
    "Obtener tarjetas asociadas a un cliente"
    #! Traerse un cliente
    #! Traerse las cuentas del cliente
    #! Buscar las tarjetas asociadas a las cuentas del cliente
    
    pass

class DireccionSerializer(serializers.ModelSerializer):
    "Modificar direccion de un cliente"
    #! Traerse un cliente
    #! Traerse las direcciones que coincidan con el campo de cliente
    pass

class PrestamosSerializer(serializers.ModelSerializer):
    "Anular la solicitud de prestamo de un cliente"
    #! Traerse un cliente
    #! Buscar los prestamos que haya hecho ese cliente
    #? ¿Como sabes cual es la solicitud de prestamo de un cliente?
    #! Eliminar el ultimo prestamo que haya hecho
    pass

class SucursalesSerializer(serializers.ModelSerializer):
    "Listado de todas las sucursales"
    #! Traerse todas las sucursales
    
    class Meta:
        model = Sucursal
        fields = "__all__"
