from ast import alias
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SolicitudPrestamoForm
from .models import Prestamo
from clientes.models import Cliente
from cuentas.models import Cuenta
from tarjetas.models import Cards



def chequearUsuarioFormulario(nombreUsuario, apellidoUsuario, dniUsuario, 
nombreFormulario, apellidoFormulario, dniFormulario):
    if nombreUsuario == nombreFormulario and apellidoUsuario == apellidoFormulario and dniUsuario == dniFormulario:
        return True
    return False
    

def chequearMonto(monto,tipo_Cliente):
    montos = {'Classic': 100000,'Gold': 300000, 'Black': 500000}
    limit = montos.get(tipo_Cliente,'')
    if monto <= limit:
        return True
    return False

"""def prestamos(request):
    form_prestamo = SolicitudPrestamoForm
    if request.method == "POST":
        form_prestamo=SolicitudPrestamoForm(data=request.POST)
        if form_prestamo.is_valid():
            #Extraer Datos de Usuario
            nameUser = request.user.first_name
            surnameUser = request.user.last_name
            dniUser = Cliente.objects.get(customer_id=Usuario.objects.get(user=request.user.id).customer_dni_id).customer_dni
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
                tipoDeCliente =TipoCliente.objects.get(tipo_clienteid = Cards.objects.get(customer_id = customer_idRecived).tipo_clienteid).tipo_cliente
                #Comprobación Monto dentro del límite
                if chequearMonto(loan_totalRecived, tipoDeCliente):
                    #Se cargan los datos a la tabla de prestamos
                    Prestamo(loan_type=loan_typeRecived, loan_date=loan_dateRecived,
                    loan_total=loan_totalRecived, customer_id =customer_idRecived).save()
                    #Se modifica el campo balance de la tabla de Cuenta
                    print('antes de crear el QS')
                    cuentaQS = Cuenta.objects.filter(customer_id=customer_idRecived)
                    print('Después de Crear el QS')
                    balancePrevio= cuentaQS.get(customer_id=customer_idRecived).balance
                    print('balance previo')
                    print(balancePrevio)
                    cuentaQS.update(balance = balancePrevio + loan_totalRecived)
                    balanceNuevo= cuentaQS.get(customer_id=customer_idRecived).balance
                    print('balance nuevo')
                    print(balanceNuevo)
                    return redirect(reverse('prestamos')+ "?ok")
                return redirect(reverse('prestamos')+ "?nomonto") 
            return redirect(reverse('prestamos')+"?nocoincide")  
        return redirect(reverse('prestamos')+ "?notok")    
    return render(request, "webitbank/pages/prestamos.html",
    {'form':form_prestamo})
# Create your views here.
"""