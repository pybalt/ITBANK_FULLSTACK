from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (status, generics, permissions)


from webitbank.models import Sucursal
from .serializers import SucursalesSerializer
# Create your views here.

class SucursalesList(generics.ListAPIView):
    
    queryset = Sucursal.objects.all()
    serializer_class = SucursalesSerializer
