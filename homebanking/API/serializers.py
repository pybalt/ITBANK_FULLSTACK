from rest_framework import serializers
"""Obtener tarjetas asociadas a un cliente❌ LECTURA!"""
from tarjetas.models import Cards
"""Modificar direccion de un cliente"""
from webitbank.models import Direcciones
from cuentas.models import Cuenta
"""Anular solicitud de prestamo de un cliente"""
from prestamos.models import Prestamo
"""Listado de todas las sucursales❌ LECTURA!"""
from webitbank.models import Sucursal

class TarjetasSerializer(serializers.ModelSerializer):
    "Obtener tarjetas asociadas a un cliente"
    #! Traerse un cliente
    #! Traerse las cuentas del cliente
    #! Buscar las tarjetas asociadas a las cuentas del cliente
    
    #* Esto ya funciona!!
    class Meta:
        model = Cards
        fields = "__all__"
        read_only_fields = ("__all__", )

    pass

class DireccionSerializer(serializers.ModelSerializer):
    "Modificar direccion de un cliente"
    #! Traerse un cliente
    #! Traerse las direcciones que coincidan con el campo de cliente
    
    #* Esto ya funciona!!
    class Meta:
        model = Direcciones
        fields = "__all__"
        read_only_fields = ("direccion_id", )


class PrestamosSerializer(serializers.ModelSerializer):
    "Anular la solicitud de prestamo de un cliente"
    #! Traerse un cliente
    #! Buscar los prestamos que haya hecho ese cliente
    #? ¿Como sabes cual es la solicitud de prestamo de un cliente?
    #! Eliminar el ultimo prestamo que haya hecho
    
    # ...
    class Meta:
        model = Sucursal
        fields = "__all__"

class SucursalesSerializer(serializers.ModelSerializer):
    "Listado de todas las sucursales"
    #! Traerse todas las sucursales
    
    #* Esto ya funciona!
    class Meta:
        model = Sucursal
        fields = "__all__"
        read_only_fields = ("__all__", )
