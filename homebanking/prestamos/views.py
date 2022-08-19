from ast import alias
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SolicitudPrestamoForm
from .models import Prestamo
from clientes.models import Cliente,Tipocliente 
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

def prestamos(request):
    form_prestamo = SolicitudPrestamoForm
    if request.method == "POST":
        form_prestamo=SolicitudPrestamoForm(data=request.POST)
        if form_prestamo.is_valid():
            #Datos A sacar de la sesion actual
            nameUser= 'Cameran'
            surnameUser = 'Castaneda'
            dniUser = '10946879'
            #Datos a comparar sacados del Formulario
            nameRecived = request.POST.get('name','')
            surnameRecived = request.POST.get('surname','')
            dniRecived = request.POST.get('dni','')
            #Otros Datos del Formulario
            loan_dateRecived = request.POST.get('startDate','')
            loan_typeRecived = request.POST.get('loan_type','')
            loan_totalRecived = int(request.POST.get('amount',''))
            print('monto:')
            print(loan_totalRecived)
            print(type(loan_totalRecived).__name__)
            #Comprobar si coincide formulario con Sesión
            if chequearUsuarioFormulario(nameUser,surnameUser,dniUser,
            nameRecived,surnameRecived,dniRecived):
                print('Coinciden datos de usuario con los de cliente')
                #Extracción del cliente a partie de nombre, apellido y dni
                cliente_filtrado = Cliente.objects.filter(customer_name=nameRecived).filter(customer_surname=surnameRecived).filter(customer_dni= dniRecived)
                print('Cliente Filtrado:')
                #print(cliente_filtrado)
                #Obtención del Customer ID
                customer_idRecived = cliente_filtrado.get(customer_dni=dniRecived).customer_id
                print('customer_idRecived:')
                print(customer_idRecived)
                #Obtención del Tipo de Cliente
                tarjeta = Cards.objects.filter(customer_id = customer_idRecived)
                tipoClienteId = tarjeta.get(customer_id = customer_idRecived).tipo_clienteid
                print(tipoClienteId)
                tipoDeClienteQS = Tipocliente.objects.filter(tipo_clienteid = tipoClienteId)
                tipoDeCliente =tipoDeClienteQS.get(tipo_clienteid = tipoClienteId).tipo_cliente
                print(tipoDeCliente)
                #Comprobación Monto dentro del límite
                if chequearMonto(loan_totalRecived, tipoDeCliente):
                    #Se cargan los datos a la tabla de prestamos
                    Prestamo(loan_type=loan_typeRecived, loan_date=loan_dateRecived,
                    loan_total=loan_totalRecived, customer_id =customer_idRecived).save()
                    #Se modifica el campo balance de la tabla de Cuenta
                    cuentasQS=Cuenta.objects.all()
                    #cuentaAmodificar = Cuenta.objects.filter(customer_id=customer_idRecived)
                    balancePrevio= cuentasQS.get(customer_id=customer_idRecived).balance
                    print('balance previo')
                    print(balancePrevio)
                    cuentasQS.filter(customer_id=customer_idRecived).update(balance = balancePrevio + loan_totalRecived)
                    return redirect(reverse('prestamos')+ "?ok")
                return redirect(reverse('prestamos')+ "?nomonto") 
            return redirect(reverse('prestamos')+"?nocoincide")  
        return redirect(reverse('prestamos')+ "?notok")    
    return render(request, "webitbank/pages/prestamos.html",
    {'form':form_prestamo})
# Create your views here.
