from django.shortcuts import render
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (status, generics, permissions) #! El permissions es para hacer autenticacion
from clientes.models import Cliente
from movimiento.models import Movimientos
from prestamos.models import Prestamo


from webitbank.models import Direcciones, Sucursal
from cuentas.models import Cuenta
from .serializers import DireccionSerializer, PrestamosSerializer, SucursalesSerializer, TarjetasSerializer
from tarjetas.models import Cards

# Create your views here.

class SucursalesList(generics.ListAPIView):
    #! ESTO FUNCIONA!!!!
    queryset = Sucursal.objects.all()
    serializer_class = SucursalesSerializer
    
    
    
"Obtener tarjetas asociadas a un cliente"
class TarjetasDelCliente(APIView):
    #! ESTO FUNCIONA!!!!
    def get(self, request, id):
    
        queryset = Cards.objects.filter(account_id__customer_id = id)
        
        serializer = TarjetasSerializer(queryset, many = True)
        
            
        return Response(serializer.data, status = status.HTTP_200_OK)
        
class ModificarDireccionCliente(APIView):
    #! ESTO FUNCIONA!!
    def get(self, request, id):
        
        queryset = Cliente.objects.get(customer_id=id).direccion
        
        serializer = DireccionSerializer(queryset)
        
            
        return Response(serializer.data, status = status.HTTP_200_OK)

    
    def put(self, request, id):
        #Cambia los datos de un objeto del libro, en funcion de su PK
        queryset = Cliente.objects.get(customer_id = id).direccion
        
        serializer = DireccionSerializer(queryset, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)
        
class ModificarSolicitudDePrestamo(APIView):
    #! ESTO FUNCIONA!!
    def delete(self, request, id):
        "Esta funcion borra la solicitud de prestamo, y actualiza el balance de la cuenta y lo registra en un movimiento"
        
        try:
            queryset = Prestamo.objects.get(loan_id = id)
            "Obtiene el prestamo con su id"
            
            if not queryset.estado == "RZD":
                    
                if queryset.estado == "APB":
                        
                    fila_cuenta = Cuenta.objects.filter(account_id = queryset.account_id)
                        
                    monto = queryset.loan_total
                    "Se guarda el monto del prestamo"
                    cuenta = queryset.account
                    "Se guarda la cuenta destino del prestamo"
                    fila_cuenta.update(balance = F('balance') - monto)
                    "Se actualiza el balance de la cuenta con el monto solicitado en el prestamo"
                        
                    cuenta_banco = Cuenta.objects.get(account_id = 1)
                        
                    movimiento = Movimientos(
                            monto = monto,
                            cuenta_remitente = cuenta,
                            cuenta_destinatario = cuenta_banco,
                        )
                        
                    movimiento.save()
                    
                    serializer = PrestamosSerializer(queryset, data = request.data)

                    queryset.delete()
                    
                    
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
                
                
                else:
                    return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)
                    
                    
            else:
                return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
                
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)    