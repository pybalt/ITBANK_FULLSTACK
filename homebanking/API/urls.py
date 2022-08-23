from .views import (ModificarDireccionCliente, ModificarSolicitudDePrestamo, SucursalesList, TarjetasDelCliente)
from django.urls import path


#ENDPOINTS DE LA API
urlpatterns = [
    #Lista de todas las sucursales
    path('sucursales/', SucursalesList.as_view()),
    #Tarjetas de un cliente
    path('tarjetas/<int:id>', TarjetasDelCliente.as_view()),
    path('direcciones/cliente/<int:id>', ModificarDireccionCliente.as_view()),
    path('direcciones/cliente/<int:id>', ModificarDireccionCliente.as_view()),
    path('prestamo/<int:id>', ModificarSolicitudDePrestamo.as_view()),
]
