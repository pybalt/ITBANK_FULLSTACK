from datetime import date
from webitbank.models import Sucursal
from prestamos.models import Prestamo
from cuentas.models import Cuenta
from webitbank.models import Direcciones
from rest_framework import serializers
from clientes.models import Cliente
"""Obtener tarjetas asociadas a un cliente❌ LECTURA!"""
from tarjetas.models import Cards
"""Modificar direccion de un cliente"""
"""Anular solicitud de prestamo de un cliente"""
"""Listado de todas las sucursales❌ LECTURA!"""


class TarjetasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        fields = "__all__"
        read_only_fields = ("__all__", )


class DireccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direcciones
        fields = "__all__"
        read_only_fields = ("direccion_id", )


class PrestamosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prestamo
        fields = "__all__"

class BorrarPrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"
        read_only_fields = ("loan_id",  "loan_type", "loan_date", "loan_total", "account", "estado")


class NuevoPrestamoSerializer(serializers.ModelSerializer):

    
    loan_date = serializers.ReadOnlyField()
    estado = serializers.ReadOnlyField()

    class Meta:
        model = Prestamo
        fields = "__all__"
        read_only_fields = ('loan_date', 'estado')


class SucursalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = "__all__"


class SaldoCuentasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuenta
        fields = ("account_id", "tipo_cuenta", "balance")

class Prestamos_TipoTotal(serializers.ModelSerializer):
    
    class Meta:
        
        model = Prestamo
        
        fields = ("loan_id", "loan_type", "loan_total")
        
        