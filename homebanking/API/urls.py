from .views import (SucursalesList)
from django.urls import path


urlpatterns = [
    #ENDPOINTS DE LA API
    path('sucursales/', SucursalesList.as_view()),
]
