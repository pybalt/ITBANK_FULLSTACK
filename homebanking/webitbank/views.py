from urllib.request import Request
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cuentas.models import Cuenta
from newsapi import NewsApiClient
from cuentas.models import Cuenta
from tarjetas.models import Cards
from movimiento.models import Movimientos
from .models import Sucursal
import requests
from clientes.models import Cliente

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
    cliente = Cliente.objects.get(user = request.user)
    cuenta_list=Cuenta.objects.filter(customer = cliente.customer_id)
    tarjeta_list=Cards.objects.filter(account__customer = cliente.customer_id)
    return render(request, "webitbank/pages/productos.html",{'cuenta_list':cuenta_list,'tarjeta_list':tarjeta_list})

@login_required
def dolar(request):
    return render(request, "webitbank/pages/dolar.html")

@login_required
def noticias(request):

    newsapi = NewsApiClient(api_key = '02f189a4f82a44539648608e1bd5ce3c')

    top_headlines = newsapi.get_top_headlines(
        category="business",
        page_size=50,
        q = "%",
        language= 'es'
    )       

    f = top_headlines["articles"]
    desc = []
    title = []
    img = []
    url = []
    for i in range(6):
        title.append(f[i]['title'])
        desc.append(f[i]['description'])
        img.append(f[i]['urlToImage'])
        url.append(f[i]['url'])
    mylist = zip(title, desc, img, url)
    context = {'mylist': mylist}
    return render(request, "webitbank/pages/noticias.html", context)


@login_required
def transferencias(request):
    cliente = Cliente.objects.get(user = request.user)
    movimiento_list=Movimientos.objects.filter(cuenta_remitente__customer = cliente)
    return render(request, "webitbank/pages/transferencias.html",{'movimiento_list':movimiento_list})

@login_required
def turnos(request):
    return render(request, "webitbank/pages/turnos.html")

@login_required
def sucursales(request):
    sucursal_list=Sucursal.objects.all()
    return render(request, "webitbank/pages/sucursales.html",{'sucursal_list':sucursal_list})

@login_required
def preguntasFrecuentes(request):
    preguntas = ['¿La cancelación anticipada tiene cargo?',
            '¿A partir de qué cuota puedo cancelar total o parcialmente el crédito inmobiliario?',
            '¿A que monto puedo acceder?',
            '¿Tiene atención al cliente?',
            '¿Puedo con un crédito hipotecario comprar un local comercial?',
            '¿Qué es un prestamo prendario?',
            ]
    respuestas = ['Cancelación total anticipada: no tiene cargo si se realiza una vez transcurrido el 25% del plazo original del crédito. (Ej. : Si Ud. tomó un crédito a 120 meses y cancela totalmente el crédito en la cuota n° 31, la cancelación no tiene cargo). Caso contrario el cargo es del 3% + IVA.',
                  'Usted podrá precancelar el crédito a partir del momento que lo desee y debe contar, por lo menos, con el importe de una cuota adicional a la que vence. Sólo podrá cancelar anticipadamente el día de vencimiento de la cuota.',
                  'El monto del crédito al cual podrá acceder será determinado en función a sus ingresos y  su capacidad de pago. Si Ud. es cliente Black podrá acceder a un prestamo de $500.000. Si Ud. es cliente Gold podrá acceder a un prestamo de $300.000. Si Ud. es cliente Classic podrá acceder a un prestamo de $100.000.',
                  'Si, puedes contactarnos',
                  'NO, solo para compra, refacción o ampliación de vivienda.',
                  'Un Préstamo Prendario es un plan de financiación para la compra de vehículos para uso particular.',
                  ]
    context = {'numero_de_preguntas':range(len(preguntas)),
               'preguntas':preguntas,
               'respuestas':respuestas}
    return render(request, "webitbank/pages/preguntasFrecuentes.html", context)

@login_required
def tarjeta_credito(request):
    user = User.objects.filter(pk = request.user.id).first()
    cliente = Cliente.objects.filter(user = user).first()
    query = Cards.objects.filter(account__customer__user = user).filter(tipo = 'CRED')
    for i in query:
        i.fecha_expiracion
        i.fecha_expiracion = i.fecha_expiracion.strftime('%m-%y')
        nro_tj = list()
        nro_tj[:0] = str(i.numero_tarjeta)
        nro_censurado = list()
        for k in nro_tj:
            nro_censurado.append('*')
        i.numero_tarjeta = ''.join(nro_censurado)
    return render(request, "webitbank/pages/card_credito.html", {"query":query, "cliente": cliente})

@login_required
def tarjeta_debito(request):
    user = User.objects.filter(pk = request.user.id).first()
    cliente = Cliente.objects.filter(user = user).first()
    query = Cards.objects.filter(account__customer__user = user).filter(tipo = 'DEB')
    for i in query:
        i.fecha_expiracion
        i.fecha_expiracion = i.fecha_expiracion.strftime('%m-%y')
        nro_tj = list()
        nro_tj[:0] = str(i.numero_tarjeta)
        nro_censurado = list()
        for _ in nro_tj:
            nro_censurado.append('*')
        i.numero_tarjeta = ''.join(nro_censurado)

    return render(request, "webitbank/pages/card_debito.html", {"query":query, "cliente":cliente})