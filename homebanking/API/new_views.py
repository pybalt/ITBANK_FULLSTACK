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
class auth(object):
    
    def __init__(self, ROL) -> None:
        "El array ROL debe de ser al menos un subconjunto de [CLIENTE, EMPLEADO, GERENTE]"
        if not(all(x in [CLIENTE, EMPLEADO, GERENTE] for x in ROL)):
            raise AttributeError("El ROL no fue asignado.") #! De no ser asi, se generara un error para 
                                                                #! Controlar mejor el codigo
        
        self.ROL = ROL
        
    def __call__(self, original_func, *args):
        "Metodo a ser llamado para decorar la instancia"
        ROL = self.ROL
        
        def wrapper(self, request, *args, **kwargs):
            for i in range(0, len(ROL)):
                "Implementado como un loop dado que aumenta la escalabilidad de este constructor"
                "Pudiendo admitir varios grupos como posibles candidatos"
                if User.objects.filter(pk = request.user.id, groups__name = ROL[i]).exists():
                    "Verifica que el usuario pertenezca al grupo del rol que asignamos"
                    return original_func(self, request, *args, **kwargs)
            return Response(status = status.HTTP_401_UNAUTHORIZED)
                
        
        return wrapper
        
    def __get__(self, instance, cls):
        "Metodo para hacer funcionar el decorador con las intancias de clase"
        return self if instance is None else MethodType(self, instance)


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

def is_member(user, ROL):
    if not ROL in (CLIENTE, EMPLEADO, GERENTE):
        raise AttributeError("El ROL no fue asignado.")
    "Verifica si un usuario pertenece a un grupo"
    return user.groups.filter(name=ROL).exists()
   

class CLIENTE_MisDatos(APIView):
    
    @auth([CLIENTE, ])
    def get(self, request):        

        current_user = request.user
        cliente = Cliente.objects.get(user=current_user)
        serializer = ClienteSerializer(cliente)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class CLIENTE_SaldoCuentas(APIView):
    @auth([CLIENTE, ])
    def get(self, request):

        cliente = Cliente.objects.get(user = request.user)
        cuenta = Cuenta.objects.filter(customer = cliente.customer_id)
        serializer = SaldoCuentasSerializer(cuenta, many = True)
                
        return Response(serializer.data, status = status.HTTP_200_OK)

    
class CLIENTE_Prestamos(APIView):
    
    @auth([CLIENTE, ])    
    def get(self, request):

        cliente = Cliente.objects.get(user = request.user)
        queryset = Prestamo.objects.filter(account__customer = cliente)
        serializer = Prestamos_TipoTotal(queryset, many = True)
                
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    
class EMPLEADO_PrestamosPorSucursal(APIView):
    
    @auth([EMPLEADO, ])    
    def get(self, request, pk):

        sucursal = Sucursal.objects.get(pk = pk)  
        queryset = Prestamo.objects.filter(account__customer__branch = sucursal)        
        serializer = PrestamosSerializer(queryset, many = True)  

        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
            

class EMPLEADO_TarjetasDelCliente(APIView):
    
    @auth([EMPLEADO, ])
    def get(self, request, pk):
        
        queryset = Cards.objects.filter(account_id__pk = pk)
        serializer = TarjetasSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)




class EMPLEADO_GenerarSolicitudDePrestamo(APIView):
    
    @auth([EMPLEADO, ])
    def post(self, request):
        if not Cuenta.objects.filter(pk = request.data['account']).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)    

        serializer = NuevoPrestamoSerializer (data = request.data)
        
        if serializer.is_valid():
            
            cuenta = request.account
            solicitud_prestamo(PRESTAMO, request.account, request.data)
            serializer.save(estado="APB",
                            loan_date = str(date.today())
                            )
            return Response(data = request.data, status = status.HTTP_200_OK)
        
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)




class EMPLEADO_AnularSolicitudDePrestamo(APIView):
    @auth([EMPLEADO, ])
    def get(self, request, id):
        
        try:
            queryset = Prestamo.objects.get(loan_id = id)
            serializer = PrestamosSerializer(queryset)
            
            return Response(serializer.data, status = status.HTTP_302_FOUND)
        
        except queryset.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    @auth([EMPLEADO, ])
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


class ModificarDireccionCliente(APIView):
    @auth([EMPLEADO, CLIENTE])
    def get(self, request, id):
        
        queryset = Cliente.objects.get(customer_id=id).direccion
        serializer = DireccionSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @auth([EMPLEADO, CLIENTE])
    def put(self, request, id):
        if is_member(request.user, CLIENTE):
            queryset = Cliente.objects.get(customer_id=request.user.id).direccion
        else:
            queryset = Cliente.objects.get(customer_id=id).direccion
            
        serializer = DireccionSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
     
        
class PUBLICA_SucursalesList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalesSerializer