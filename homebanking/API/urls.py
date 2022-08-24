from .views import (EMPLEADO_CrearSolicitudPrestamo, CLIENTE_DatosPropios, EMPLEADO_ModificarDireccionCliente, EMPLEADO_BorrarSolicitudPrestamo, PUBLICA_SucursalesList, EMPLEADO_TarjetasDelCliente)
from django.urls import path


#ENDPOINTS DE LA API
urlpatterns = [
    #Lista de todas las sucursales
    path('sucursales/', PUBLICA_SucursalesList.as_view()),
    #Un empleado puede ver las tarjetas de un cliente con su ID
    path('tarjetas/<int:id>', EMPLEADO_TarjetasDelCliente.as_view()),
    #Un empleado puede modificar la direccion de un cliente con su ID
    path('direcciones/cliente/<int:id>', EMPLEADO_ModificarDireccionCliente.as_view()),
    path('prestamo/borrar/<int:id>', EMPLEADO_BorrarSolicitudPrestamo.as_view()),
    path('prestamo/crear/', EMPLEADO_CrearSolicitudPrestamo.as_view()),
    
    path('cliente/', CLIENTE_DatosPropios.as_view()),
]
