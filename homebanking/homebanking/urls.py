"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webitbank import views
from prestamos.views import prestamosDetails


urlpatterns = [
    path('admin/',              admin.site.urls),
    path('login/',              views.login,                                name="login"),
    path('',                    views.home,                                 name="home"),
    path('pagoServicios/',      views.pagoServicios,                        name="pagoServicios"),
    path('productos/',          views.productos,                            name="productos"),
    path('dolar/',              views.dolar,                                name="dolar"),
    path('noticias/',           views.noticias,                             name="noticias"),
    #path('prestamos/',         views.prestamos,                            name="prestamos"),
    path('prestamos/',          include('prestamos.urls')),
    path('sucursales/',         views.sucursales,                              name="sucursales"),
    path('transferencias/',     views.transferencias,                       name="transferencias"),
    path('turnos/',             views.turnos,                               name="turnos"),
    path('accounts/',           include('django.contrib.auth.urls')),
    path('api/', include('API.urls'))
]