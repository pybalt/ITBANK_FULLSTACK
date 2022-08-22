from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (status, generics, permissions)


from webitbank.models import Sucursal
from .serializers import SucursalesSerializer
# Create your views here.

class SucursalesList(APIView):
    
    def get(self, request):
        
        sucursales = Sucursal.objects.all().order_by('branch_id')
        serializer = SucursalesSerializer(sucursales, many = True)
        
        return Response(serializer.data, status = status.HTTP_200_OK)