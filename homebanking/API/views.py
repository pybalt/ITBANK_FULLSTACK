from queue import Empty
from urllib import request
from django.db.models import F  # Para actualizar un campo de la base de datos
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
# ! El permissions es para hacer autenticacion
from rest_framework import (status, generics)
from clientes.models import Cliente
from movimiento.models import Movimientos
from prestamos.models import Prestamo
from types import MethodType # Para crearle decoradores a las clases
from rest_framework.renderers import TemplateHTMLRenderer
from webitbank.models import Sucursal
from cuentas.models import Cuenta
from .serializers import *
from tarjetas.models import Cards

CLIENTE = "Cliente"
EMPLEADO = "Empleado"
GERENTE = "Gerente"
PRESTAMO = "PR"
REVERTIR_PRESTAMO = "PR_REVERT"

"DECORADOR DE AUTENTICACION"
from .custom_permissions import *


def solicitud_prestamo(tipo_movimiento, cuenta, prestamo):
    if not tipo_movimiento in (PRESTAMO, REVERTIR_PRESTAMO):
        raise AttributeError("No se reconoce el tipo de movimiento")
    
    if isinstance(cuenta, int):
        #si cuenta es un objeto
        cuenta = cuenta
    else:
        cuenta = cuenta.account_id
        
    if isinstance(prestamo, dict):
        monto = prestamo['loan_total']
        cuenta_destino = prestamo['account']
    else:
        monto = prestamo.loan_total
        cuenta_destino = prestamo.account.account_id
    
    
    fila_cuenta = Cuenta.objects.filter(account_id = cuenta)          
    cuenta = Cuenta.objects.get(account_id = cuenta_destino)       
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


def is_member(user, ROL):
    if not ROL in (CLIENTE, EMPLEADO, GERENTE):
        raise AttributeError("El ROL no fue asignado.")
    "Verifica si un usuario pertenece a un grupo"
    return user.groups.filter(name=ROL).exists()
   

class CLIENTE_MisDatos(APIView):
    
    permission_classes = [AuthenticatedClient]
    
    def get(self, request):        

        current_user = request.user
        cliente = Cliente.objects.get(user=current_user)
        serializer = ClienteSerializer(cliente)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class CLIENTE_SaldoCuentas(APIView):
    permission_classes = [AuthenticatedClient]
    
    def get(self, request):

        cliente = Cliente.objects.get(user = request.user)
        cuenta = Cuenta.objects.filter(customer = cliente.customer_id)
        serializer = SaldoCuentasSerializer(cuenta, many = True)
                
        return Response(serializer.data, status = status.HTTP_200_OK)

    
class CLIENTE_Prestamos(APIView):
    permission_classes = [AuthenticatedClient]
      
    def get(self, request):
        cliente = Cliente.objects.get(user = request.user)
        queryset = Prestamo.objects.filter(account__customer = cliente)
        serializer = Prestamos_TipoTotal(queryset, many = True)
                    
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
      


    
class EMPLEADO_PrestamosPorSucursal(APIView):
    
    permission_classes = [AuthenticatedEmployee]  
    def get(self, request, pk):
        try:

            sucursal = Sucursal.objects.get(pk = pk)  
            queryset = Prestamo.objects.filter(account__customer__branch = sucursal)        
            serializer = PrestamosSerializer(queryset, many = True)  

            return Response(serializer.data, status = status.HTTP_200_OK)
        except Sucursal.DoesNotExist:
            print("La sucursal no existe")
            return Response(status = status.HTTP_404_NOT_FOUND)

    
class EMPLEADO_TarjetasDelCliente(APIView):

    permission_classes = [AuthenticatedEmployee] 
    def get(self, request, pk):
        queryset = Cards.objects.filter(account_id__pk = pk).filter(tipo = "CRED")
        if not len(queryset)==0:
            serializer = TarjetasSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("No hay tarjetas de creditos para ese cliente")
            return Response(status = status.HTTP_404_NOT_FOUND)
        


        




class EMPLEADO_GenerarSolicitudDePrestamo(APIView):
    permission_classes = [AuthenticatedEmployee]  
    
    def post(self, request):
        try:
            if not Cuenta.objects.filter(pk = request.data['account']).exists():
                
                return Response(status = status.HTTP_404_NOT_FOUND)


            serializer = NuevoPrestamoSerializer (data = request.data)
            
            if serializer.is_valid():
                
                cuenta = request.data['account']
                solicitud_prestamo(PRESTAMO, request.data['account'], request.data)
                serializer.save(estado="APB",
                                loan_date = str(date.today())
                                )
                return Response(data = request.data, status = status.HTTP_200_OK)
            
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            print("La solicitud no tiene parametros")
            return Response(status = status.HTTP_400_BAD_REQUEST)




class EMPLEADO_AnularSolicitudDePrestamo(APIView):
    permission_classes = [AuthenticatedEmployee]  
    def get(self, request, id):
        
        try:
            queryset = Prestamo.objects.get(loan_id = id)
            serializer = PrestamosSerializer(queryset)
            
            return Response(serializer.data, status = status.HTTP_302_FOUND)
        
        except queryset.DoesNotExist:
            print("No existe prestamo para borrar")
            return Response(status = status.HTTP_404_NOT_FOUND)


    def delete(self, request, id):
        try:
            prestamo = Prestamo.objects.get(loan_id = id)
            "Obtiene el prestamo con su id"
            if prestamo.estado == "RZD":
                return Response(status = status.HTTP_406_NOT_ACCEPTABLE)

            if prestamo.estado in ("APB", "PDT"):
                serializer = BorrarPrestamoSerializer(
                        prestamo, data = request.data)
               
                if serializer.is_valid():

                    solicitud_prestamo(REVERTIR_PRESTAMO, prestamo.account, prestamo)
                    serializer.save(
                        loan_id = prestamo.loan_id,  
                        loan_type = prestamo.loan_type, 
                        loan_date = prestamo.loan_date, 
                        loan_total = prestamo.loan_total, 
                        account = prestamo.account, 
                        estado = prestamo.estado
                    )
                    prestamo.delete()
                    
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

                else:
                    print(serializer.errors)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ModificarDireccionCliente(APIView):
    permission_classes = [AuthenticatedEmployee|AuthenticatedClient]
    def get(self, request, id):
        
        queryset = Cliente.objects.get(customer_id=id).direccion
        serializer = DireccionSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, id):
        if is_member(request.user, CLIENTE):
            queryset = Cliente.objects.get(user_id = request.user.id).direccion
        else:
            try:
                queryset = Cliente.objects.get(user_id = id).direccion
            except Cliente.DoesNotExist:
                print("El cliente no existe")
                return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = DireccionSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
     
        
class PUBLICA_SucursalesList(generics.ListAPIView):

    
    def get(self, request): 
        queryset = Sucursal.objects.all()
        serializer_class = SucursalesSerializer(queryset,many=True)
        return Response(serializer_class.data,status=status.HTTP_202_ACCEPTED)