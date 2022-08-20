from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, "registration/login.html")

@login_required
def home(request):
    return render(request, "webitbank/home.html")

@login_required
def pagoServicios(request):
    return render(request, "webitbank/pages/pago_servicios.html")

@login_required
def productos(request):
    return render(request, "webitbank/pages/productos.html")

@login_required
def dolar(request):
    return render(request, "webitbank/pages/dolar.html")

@login_required
def noticias(request):
    return render(request, "webitbank/pages/noticias.html")

@login_required
def prestamos(request):
    return render(request, "webitbank/pages/prestamos.html")

@login_required
def transferencias(request):
    return render(request, "webitbank/pages/transferencias.html")

@login_required
def turnos(request):
    return render(request, "webitbank/pages/turnos.html")

@login_required
def seguros(request):
    return render(request, "webitbank/pages/seguros.html")