from dataclasses import fields
from email.policy import default
from wsgiref.handlers import format_date_time
from django import forms
from .models import Prestamo
from cuentas.models import Cuenta
from .choices import tipo_prestamo as tipo
from django.contrib.admin import widgets 

class SolicitudPrestamoForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label= 'Nombres', required=True)
    surname = forms.CharField(max_length=50, label= 'Apellidos', required=True)
    dni= forms.IntegerField(label= 'DNI', required= True)
    class Meta:
        model=Prestamo
        fields = ['name','surname','dni','loan_date','loan_type','loan_total']#