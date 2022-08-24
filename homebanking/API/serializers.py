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


class NuevoPrestamoSerializer(serializers.ModelSerializer):

    loan_date = serializers.ReadOnlyField(source=str(date.today()))
    print(loan_date)

    class Meta:
        model = Prestamo
        fields = "__all__"
        read_only_fields = ('loan_date', )


class SucursalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = "__all__"


class CuentaSerializer(serializers.ModelSerializer):

    def get_fields(self):
        fields = super().get_fields()
        for field in fields.values():
            field.read_only = True

        return fields

    class Meta:
        model = Cuenta
        fields = "__all__"
        read_only_fields = ("account_id",
                            "customer",
                            "balance",
                            "tipo_cuenta",
                            "iban",)
