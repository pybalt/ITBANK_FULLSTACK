from urllib.request import Request
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from cuentas.models import Cuenta
from .models import Sucursal
import requests

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
    cuenta_list=Cuenta.objects.all()
    return render(request, "webitbank/pages/productos.html",{'cuenta_list':cuenta_list})

@login_required
def dolar(request):
    return render(request, "webitbank/pages/dolar.html")

@login_required
def noticias(request):
    url = 'https://newsapi.org/v2/everything?q=Cryptocurrency&from=2022-08-01&sortBy=popularity&apiKey=533ada2ab21546568011c689d22edda6'
    crypto_news = requests.get(url).json()
    a = crypto_news['articles']
    desc = []
    title = []
    img = []
    url = []
    for i in range(5):
            f = a[i]
            title.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
            url.append(f['url'])
    mylist = zip(title, desc, img, url)
    context = {'mylist': mylist}
    return render(request, "webitbank/pages/noticias.html", context)


@login_required
def transferencias(request):
    return render(request, "webitbank/pages/transferencias.html")

@login_required
def turnos(request):
    return render(request, "webitbank/pages/turnos.html")

@login_required
def sucursales(request):
    sucursal_list=Sucursal.objects.all()
    return render(request, "webitbank/pages/sucursales.html",{'sucursal_list':sucursal_list})

@login_required
def preguntasFrecuentes(request):
    return render(request, "webitbank/pages/preguntasFrecuentes.html")


