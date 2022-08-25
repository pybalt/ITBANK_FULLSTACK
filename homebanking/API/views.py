from urllib import request
from django.shortcuts import render
from django.db.models import F  # Para actualizar un campo de la base de datos
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
# ! El permissions es para hacer autenticacion
from rest_framework import (status, generics)
from clientes.models import Cliente
from movimiento.models import Movimientos
from prestamos.models import Prestamo


from webitbank.models import Sucursal
from cuentas.models import Cuenta
from .serializers import *
from tarjetas.models import Cards

# Create your views here.

"Grupos"
CLIENTE = "Cliente"
EMPLEADO = "Empleado"
GERENTE = "Gerente"

class PUBLICA_SucursalesList(generics.ListAPIView):
    #! ESTO FUNCIONA!!!!
    pass


class EMPLEADO_TarjetasDelCliente(APIView):
    
        
    #! ESTO FUNCIONA!!!!
    pass


class EMPLEADO_ModificarDireccionCliente(APIView):
    
    pass



def movimientosBD(request, prestamo, op, tipo):
    """ Actualiza el valor de la base de datos y genera un movimiento registrando dicho cambio
    queryset puede ser request.data o una instancia de la clase PRESTAMO
    OP puede ser RESTA o SUMA
    TIPO puede ser o bien revert o bien PR
    """
    if not tipo in ("revert", "PR"):
        raise TypeError("La variable tipo no esta bien definida")
    match op:
        case 'RESTA':
            fila_cuenta.update(balance=F('balance') - monto)
        case 'SUMA':
            fila_cuenta.update(balance=F('balance') + monto)
        case _:
            raise TypeError("La variable OP no esta bien definida")
    
    fila_cuenta = Cuenta.objects.filter(account_id = prestamo.account_id)
    monto = prestamo.loan_total
    "Se guarda el monto del prestamo"
    cuenta = prestamo.account
    "Se guarda la cuenta destino del prestamo"
        
    cuenta_banco = Cuenta.objects.get(account_id = 1)

    tipomov = "PR_REVERT" if tipo == "revert" else "PR"

    movimiento = Movimientos(
        monto = monto,
        cuenta_remitente = cuenta,
        cuenta_destinatario = cuenta_banco,
        tipo_movimiento = tipomov
    )

    serializer = PrestamosSerializer(
        prestamo, data = request.data)
    
    return serializer, movimiento


class EMPLEADO_BorrarSolicitudPrestamo(APIView):
    
            
    def get(self, request, id):
        
        try:
            queryset = Prestamo.objects.get(loan_id = id)
            serializer = PrestamosSerializer(queryset)
            
            return Response(serializer.data, status = status.HTTP_302_FOUND)
        
        except queryset.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
            
    
    
    
    def delete(self, request, id):
        
        try:
            prestamo = Prestamo.objects.get(loan_id = id)
            "Obtiene el prestamo con su id"

            if prestamo.estado == "RZD":
                return Response(status = status.HTTP_406_NOT_ACCEPTABLE)

            if prestamo.estado in ("APB", "PDT"):

                serializer = PrestamosSerializer(
                        prestamo, data = request.data)
               
                if serializer.is_valid():

                    solicitud_prestamo(REVERTIR_PRESTAMO, prestamo.account, prestamo)
                    serializer.save()
                    
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

                else:
                    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EMPLEADO_CrearSolicitudPrestamo(APIView):
    pass

class CLIENTE_DatosPropios(APIView):
   pass

class CLIENTE_SaldoCuentas(APIView):
    
    "Un cliente [autenticado] puede obtener el tipo de cuenta y su saldo"    
    pass
            
class CLIENTE_PrestamosCuentas(APIView):
    
    "Un cliente [autenticado] puede obtener sus prestamos: El tipo de prestamo y el total del mismo"

        

class EMPLEADO_PrestamosPorSucursal(APIView):
    pass


"CONSTANTES A PASARLE A LA FUNCION"
PRESTAMO = "PR"
REVERTIR_PRESTAMO = "PR_REVERT"

def solicitud_prestamo(tipo_movimiento, cuenta, prestamo):
    
    if not tipo_movimiento in (PRESTAMO, REVERTIR_PRESTAMO):
        raise AttributeError("No se reconoce el tipo de movimiento")
    
    fila_cuenta = Cuenta.objects.filter(account_id = cuenta)
                    
    monto = prestamo.loan_total

    cuenta = prestamo.account
                    
                            
    cuenta_banco = Cuenta.objects.get(account_id = 1)
    
    if tipo_movimiento == PRESTAMO:
        fila_cuenta.update(balance= F('balance') + monto)
    else:
        fila_cuenta.update(balance= F('balance') - monto)
   

    movimiento = Movimientos(
                            monto = monto,
                            cuenta_remitente = cuenta,
                            cuenta_destinatario = cuenta_banco,
                            tipo_movimiento = tipo_movimiento
                        )

    movimiento.save()
    prestamo.delete()


       