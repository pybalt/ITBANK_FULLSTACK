from ast import alias
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SolicitudPrestamoForm
from .models import Prestamo
from clientes.models import Cliente
from cuentas.models import Cuenta
from tarjetas.models import Cards
from django.contrib.auth.models import User 
from movimiento.models import Movimientos
import datetime

def chequearUsuarioFormulario(nombreUsuario, 
                              apellidoUsuario, 
                              dniUsuario, 
                              nombreFormulario, 
                              apellidoFormulario, 
                              dniFormulario):
    return (nombreUsuario == nombreFormulario 
    and apellidoUsuario == apellidoFormulario 
    and dniUsuario == dniFormulario)
    

def chequearMonto(monto,tipo_Cliente):
    montos = {'CLS': 100000,'GLD': 300000, 'BLK': 500000}
    limit = montos.get(tipo_Cliente,'')
    return monto <= limit

def prestamosView(request):
    print('hola1')
    form_prestamo = SolicitudPrestamoForm
    if request.method == "POST":
        form_prestamo=SolicitudPrestamoForm(data = request.POST)
        if form_prestamo.is_valid():
            #Extraer Datos de Usuario
            try:
                cliente=Cliente.objects.get(user=request.user)
            except Cliente.DoesNotExist:
                return redirect(reverse('prestamos')+"?nocliente")
            nameUser = cliente.customer_name
            surnameUser = cliente.customer_surname
            dniUser = str(cliente.customer_dni)
            print(nameUser)
            print(surnameUser)
            print(dniUser)
            #Datos a comparar sacados del Formulario
            nameRecived = request.POST.get('name','')
            surnameRecived = request.POST.get('surname','')
            dniRecived = request.POST.get('dni','')
            #Otros Datos del Formulario
            loan_dateRecived = request.POST.get('startDate','')
            loan_typeRecived = request.POST.get('loan_type','')
            loan_totalRecived = int(request.POST.get('amount',''))
            #Comprobar si coincide formulario con Sesión
            if chequearUsuarioFormulario(nameUser,surnameUser,dniUser,
            nameRecived,surnameRecived,dniRecived):
                print('Coinciden datos de usuario con los de cliente')      
                customer_idRecived = Cliente.objects.filter(customer_name=nameRecived).filter(customer_surname=surnameRecived).get(customer_dni= dniRecived).customer_id
                #Comprobación Monto dentro del límite
                print(cliente.tipo)
                print(type(cliente.tipo))
                if chequearMonto(loan_totalRecived, cliente.tipo):
                    #Se cargan los datos a la tabla de prestamos
                    try:
                        cuenta = Cuenta.objects.filter(tipo_cuenta= 'CAP').get(customer=cliente)
                    except Cliente.DoesNotExist:
                        return redirect(reverse('prestamos')+"?nocuenta")
                    prestamo=Prestamo(loan_type=loan_typeRecived, loan_date=loan_dateRecived,
                    loan_total=loan_totalRecived, account =cuenta, estado = 'APB')
                    prestamo.save()
                    #Se modifica el campo balance de la tabla de Cuenta
                    print('balance previo')
                    print(cuenta.balance)
                    cuenta.update(balance=F('balance')+loan_totalRecived)
                    print('balance nuevo')
                    print(cuenta.balance)
                    #Se registra el movimiento
                    cuenta_banco= Cuenta.objects.get(account_id = 1)
                    movimiento = Movimientos(
                            monto = loan_totalRecived,
                            cuenta_remitente = cuenta_banco,
                            cuenta_destinatario = cuenta,
                            tipo_movimiento = 'PR'
                            )
                    movimiento.save()
                    return redirect(reverse('prestamos')+ "?ok")
                else:
                    return redirect(reverse('prestamos')+ "?nomonto") 
            
            return redirect(reverse('prestamos')+"?nocoincide")  
        
        return redirect(reverse('prestamos')+ "?notok")    
    
    return render(request, "webitbank/pages/prestamos.html",
    {'form':form_prestamo})