from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SolicitudPrestamoForm
from .models import Prestamo
from clientes import models as cliente_models
import datetime

def chequearUsuarioFormulario(nombreUsuario, apellidoUsuario, dniUsuario, 
nombreFormulario, apellidoFormulario, dniFormulario):
    if nombreUsuario == nombreFormulario and apellidoUsuario == apellidoFormulario and dniUsuario == dniFormulario:
        return True
    return False
    

def chequearMonto(monto,tipo_Cliente):
    montos = {'Classic': 100000,'Gold': 300000, 'Black': 500000}
    if monto <= montos.get(tipo_Cliente,''):
        return True
    return False

def prestamos(request):
    form_prestamo = SolicitudPrestamoForm
    if request.method == "POST":
        if form_prestamo.is_valid():
            #Datos A sacar de la sesion actual
            nameUser= 'pepe'
            surnameUser = 'perez'
            dniUser = 11111111
            #Datos a comparar sacados del Formulario
            nameRecived = request.POST.get('Nombres','')
            surnameRecived = request.POST.get('Apellidos','')
            dniRecived = request.POST.get('DNI','')
            #Otros Datos del Formulario
            loan_dateRecived = request.POST.get('Fecha de Inicio','')
            loan_typeRecived = request.POST.get('Tipo de Préstamo','')
            loan_totalRecived = request.POST.get('Monto del Prestamo','')
            #Formateo de Fecha
            loan_dateRecivedString = loan_dateRecived.strftime('%d/%m/%Y')
            #Comprobar si coincide formulario con Sesión
            if chequearUsuarioFormulario(nameUser,surnameUser,dniUser,
            nameRecived,surnameRecived,dniRecived):
                #Extracción del cliente a partie de nombre, apellido y dni
                cliente_filtrado = cliente_models.objects.filter(customer_name=nameRecived).filter(customer_surname=surnameRecived).filter(custumer_dni= dniRecived)
                #Obtención del Customer ID
                customer_idRecived = cliente_filtrado.get('customer_id','')
                print(customer_idRecived)
                #Obtención del Tipo de Cliente
                tipoDeCliente = cliente_filtrado.get('tipo_cliente','')
                #Comprobación Monto dentro del límite
                if chequearMonto(loan_totalRecived, tipoDeCliente):
                    Prestamo(loan_type=loan_typeRecived, loan_date=loan_dateRecived,
                    loan_total=loan_totalRecived, customer_id =customer_idRecived)
                    return redirect(reverse('prestamos')+ "?ok")
                return redirect(reverse('prestamos')+ "?nomonto")


                
                


            
            
            
        else: 
            return redirect(reverse('prestamos')+ "?notok")    
    return render(request, "prestamos/prestamos.html",
    {'form':form_prestamo})
# Create your views here.
