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
from datetime import datetime
"""



"Se recibe año, mes, dia"
dato_recibido = "2016-04-14"

dato_recibido = datetime.strptime(dato_recibido, "%Y-%m-%d") #Crea un objeto con el formato especificado

dato_recibido = datetime.strftime(dato_recibido, "%d-%m-%Y")

print(dato_recibido, type(dato_recibido))"""

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
    mensaje="""Formato correcto de Fecha: día/mes/Año Completo"""
    if request.method == "POST":
        form_prestamo=SolicitudPrestamoForm(data = request.POST)
        if form_prestamo.is_valid():
            #Extraer Datos de Usuario
            try:
                cliente=Cliente.objects.get(user=request.user)
            except Cliente.DoesNotExist:
                mensaje="""el usuario no tiene ningún cliente asociado"""
                #return redirect(reverse('prestamos')+"?nocliente")
            nameUser = cliente.customer_name
            surnameUser = cliente.customer_surname
            dniUser = str(cliente.customer_dni)
            print(nameUser)
            print(surnameUser)
            print(type(dniUser))
            #Datos a comparar sacados del Formulario
            nameRecived = request.POST.get('name','')
            surnameRecived = request.POST.get('surname','')
            dniRecived = request.POST.get('dni','')
            #Otros Datos del Formulario
            loan_dateRecived = request.POST.get('loan_date','')
            try:
                loan_dateRecived = datetime.strptime(loan_dateRecived, "%d/%m/%Y")
                print(loan_dateRecived)
                loan_dateRecived = datetime.strftime(loan_dateRecived,'%Y-%m-%d')
            except:
                mensaje= """Formato de fecha Incorrecto. """ +mensaje
                #return redirect(reverse('prestamos')+"?formatofecha")
            loan_typeRecived = request.POST.get('loan_type','')
            loan_totalRecived = int(request.POST.get('loan_total',''))
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
                        mensaje = """Usted no posee una caja de ahorro en pesos"""
                        #return redirect(reverse('prestamos')+"?nocuenta")
                    prestamo=Prestamo(loan_type=loan_typeRecived, loan_date=loan_dateRecived,
                    loan_total=loan_totalRecived, account =cuenta, estado = 'APB')
                    
                    try:
                        prestamo.save() 
                    except:
                        mensaje="""Error al registrar el préstamo."""
                        #return redirect(reverse('prestamos')+"?noprestamo")
                    #Se modifica el campo balance de la tabla de Cuenta
                    print('balance previo')
                    print(cuenta.balance)
                    cuenta.balance = cuenta.balance+loan_totalRecived
                    cuenta.save(update_fields=['balance'])
                    print('balance nuevo')
                    print(cuenta.balance)
                    #Se registra el movimiento
                    cuenta_banco= Cuenta.objects.get(account_id = 1)
                    cuenta_banco.balance=cuenta_banco.balance-loan_totalRecived
                    cuenta_banco.save(update_fields=['balance'])
                    movimiento = Movimientos(
                            monto = loan_totalRecived,
                            cuenta_remitente = cuenta_banco,
                            cuenta_destinatario = cuenta,
                            tipo_movimiento = 'PR'
                            )
                    movimiento.save()
                    mensaje="""Su prestamo ha sido aceptado, el saldo de su cuenta ya fue actualizado"""
                    #return redirect(reverse('prestamos')+ "?ok")
                else:
                    mensaje="""El monto solicitado supera el límite establecido para su cuenta.
            Los límites son: 500000 para clientes Black, 300000 para clientes Gold y 10000 para clientes Classic"""
                    #return redirect(reverse('prestamos')+ "?nomonto") 
            else:
                mensaje="""Los datos ingresados en el formulario no coincide con los asociados al usuario logueado. 
            Recuerde que solo puede solicitar el prestamo desde el usuario asociado a la cuenta en la que desea recibir el dinero"""
                #return redirect(reverse('prestamos')+"?nocoincide")  
        
        else:
            mensaje= """lguno de los campos ingresados no es válido"""
            #return redirect(reverse('prestamos')+ "?notok")    
    diccionario = {'form':form_prestamo,'msj':mensaje}
    return render(request, "prestamos/prestamos.html",
    diccionario)