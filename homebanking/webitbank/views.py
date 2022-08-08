
from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    """ html_response = "<h1>Bienvenidos a mi sitio de prueba</h1>"
    for i in range(10):
        html_response += "<p>pito " + str(i) + "</p>"
    return HttpResponse(html_response) """
    return render(request, "webitbank/index.html")

def pagoServicios(request):
    """ html_response = "<h1>Bienvenidos a mi sitio de prueba</h1>"
    for i in range(10):
        html_response += "<p>pito " + str(i) + "</p>"
    return HttpResponse(html_response) """
    return render(request, "webitbank/pages/pago_servicios.html")

def productos(request):
    return render(request, "webitbank/pages/productos.html")

def dolar(request):
    return render(request, "webitbank/pages/dolar.html")

def noticias(request):
    return render(request, "webitbank/pages/noticias.html")
def prestamos(request):
    return render(request, "webitbank/pages/prestamos.html")
def transferencias(request):
    return render(request, "webitbank/pages/transferencias.html")
def turnos(request):
    return render(request, "webitbank/pages/turnos.html")
def seguros(request):
    return render(request, "webitbank/pages/seguros.html")