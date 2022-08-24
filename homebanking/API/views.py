from django.shortcuts import render
from django.db.models import F  # Para actualizar un campo de la base de datos
from rest_framework.views import APIView
from rest_framework.response import Response
# ! El permissions es para hacer autenticacion
from rest_framework import (status, generics, permissions)
from clientes.models import Cliente
from movimiento.models import Movimientos
from prestamos.models import Prestamo


from webitbank.models import Sucursal
from cuentas.models import Cuenta
from .serializers import *
from tarjetas.models import Cards

# Create your views here.


class PUBLICA_SucursalesList(generics.ListAPIView):
    #! ESTO FUNCIONA!!!!
    queryset = Sucursal.objects.all()
    serializer_class = SucursalesSerializer


class EMPLEADO_TarjetasDelCliente(APIView):
    
    "Un empleado [falta autenticacion] puede ver las tarjetas asociadas a un cliente"
        
    #! ESTO FUNCIONA!!!!
    def get(self, request, id):  # ? Que pasa si borro el request? #TODO Testear

        queryset = Cards.objects.filter(account_id__customer_id=id)

        serializer = TarjetasSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EMPLEADO_ModificarDireccionCliente(APIView):
    
    "Un empleado [falta autenticacion] puede modificar la direccion de un cliente proporcionando una ID"
    
    def get(self, request, id):
        # Obtiene la direccion de un cliente
        queryset = Cliente.objects.get(customer_id=id).direccion

        serializer = DireccionSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        # Cambia la direccion de un cliente
        queryset = Cliente.objects.get(customer_id=id).direccion

        serializer = DireccionSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)



def movimientosBD(request, queryset):
    """ Actualiza el valor de la base de datos y genera un movimiento registrando dicho cam"""
    
    fila_cuenta = Cuenta.objects.filter(account_id=queryset.account_id)
    monto = queryset.loan_total
    "Se guarda el monto del prestamo"
    cuenta = queryset.account
    "Se guarda la cuenta destino del prestamo"
    fila_cuenta.update(balance=F('balance') - monto)
    "Se actualiza el balance de la cuenta con el monto solicitado en el prestamo"
    cuenta_banco = Cuenta.objects.get(account_id=1)

    movimiento = Movimientos(
        monto=monto,
        cuenta_remitente=cuenta,
        cuenta_destinatario=cuenta_banco,
    )

    movimiento.save()

    serializer = PrestamosSerializer(
        queryset, data=request.data)
    return serializer


class EMPLEADO_BorrarSolicitudPrestamo(APIView):
    
    "Un empleado [falta autenticacion] puede borrar una solicitud de prestamo"
    def get(self, id):
        try:
            queryset = Prestamo.objects.get(loan_id = id)
            serializer = PrestamosSerializer(queryset)
        
            return Response(serializer.data, status = status.HTTP_302_FOUND)
        
        except queryset.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
            
    
    
    
    def delete(self, request, id):

        try:
            queryset = Prestamo.objects.get(loan_id=id)
            "Obtiene el prestamo con su id"

            if not queryset.estado == "RZD":

                if queryset.estado == "APB":

                    serializer = movimientosBD(request, queryset)
                    queryset.delete()

                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

                else:
                    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EMPLEADO_CrearSolicitudPrestamo(APIView):
    
    "Un empleado [falta autenticacion] puede crear un prestamo"
    "Crea una solicitud de prestamo APROBADO"

    def post(self, request):  # TODO HACER POST
        serializer = NuevoPrestamoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(estado="APB")

            return Response(data=request.data, status=status.HTTP_200_OK)
        
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class CLIENTE_DatosPropios(APIView):

    def get(self, request):
        "Lo hace con el usuario que esta log"
        try:

            current_user = request.user
            cliente = Cliente.objects.get(user=current_user)
            serializer = ClienteSerializer(cliente, data=...)

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        except cliente.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

class CLIENTE_ModificarDireccionCliente(APIView):
    pass