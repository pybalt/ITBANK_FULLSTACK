from .views import *

from django.urls import path


# ENDPOINTS DE LA API
urlpatterns = [
    # Un cliente autenticado puede consultar sus propios datos
    path('cliente/misdatos/', CLIENTE_MisDatos.as_view(), name = "MIS DATOS"),
    
    # Un cliente autenticado puede obtener el tipo de cuenta y su saldo
    path('cliente/misdatos/cuentas/', CLIENTE_SaldoCuentas.as_view(), name = "CUENTA, TIPO Y SALDO"),
   
    # Un cliente autenticado puede obtener el tipo de prestamo y total de los mismos
    path('cliente/misdatos/prestamos/', CLIENTE_Prestamos.as_view(), name = "PRESTAMOS, TIPO Y TOTAL"),
    
    # Un empleado autenticado puede obtener el listado de prestamos
    #   otorgados de una sucursal determinada
    path('empleado/prestamos/sucursal/<int:pk>', EMPLEADO_PrestamosPorSucursal.as_view(), name = "PRESTAMOS POR SUCURSAL"),
    
    # Un empleado autenticado puede obtener el listado de tarjetas
    #   de credito de un cliente determinado
    path('empleado/cliente/tarjetas/<int:pk>', EMPLEADO_TarjetasDelCliente.as_view(), name = "TARJETAS DE CREDITO POR CLIENTE"),
    
    # Un empleado autenticado puede solicitad un prestamo para un cliente
    #   Registrando el mismo (generando un movimiento)
    #       Y acreditando el saldo en su cuenta
    path('empleado/cliente/otorgarprestamo/', EMPLEADO_GenerarSolicitudDePrestamo.as_view(), name = "OTORGAR PRESTAMOS"),
    
    # Un empleado autenticado puede anular un prestamo para un cliente
    #   Revirtiendo el monto correspondiente
    path('empleado/cliente/quitarprestamo/<int:id>', EMPLEADO_AnularSolicitudDePrestamo.as_view(), name = "REVERTIR PRESTAMO"),
    
    # El propio cliente autenticado o un empleado puede modificar las direcciones
    path('cliente/modificardireccion/<int:id>', ModificarDireccionCliente.as_view(), name = "MODIFICAR DIRECCION"),
    
    # Un endpoint publico que devuelve el listado de todas las sucursales
    #   con la informacion correspondiente
    path('sucursales/lista', PUBLICA_SucursalesList.as_view(), name = 'PUBLICA'),

]
