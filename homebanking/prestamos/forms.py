from dataclasses import fields
from email.policy import default
from wsgiref.handlers import format_date_time
from django import forms
from .models import Prestamo
from cuentas.models import Cuenta
from .choices import tipo_prestamo as tipo
"""
class SolicitudPrestamoForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label= 'Nombres', required=True)
    surname = forms.CharField(max_length=50, label= 'Apellidos', required=True)
    dni= forms.IntegerField(label= 'DNI', required= True)
    account= forms.ChoiceField(queryset )
    class Meta:
        model=Prestamo
        fields = ['loan_type','loan_date','loan_total']
"""
class SolicitudPrestamoForm(forms.Form):
    name = forms.CharField(max_length=50, label= 'Nombres', required=True)
    surname = forms.CharField(max_length=50, label= 'Apellidos', required=True)
    dni= forms.IntegerField(label= 'DNI', required= True)
    #account= forms.ChoiceField(queryset )
    startDate = forms.DateField(label = 'Fecha de Inicio', required=True, widget=forms.SelectDateWidget(format="%d %b %Y"))
    loan_type = forms.ChoiceField(label = 'Tipo de Préstamo', required=True, choices= tipo)
    amount = forms.IntegerField(label = 'Monto del Préstamo', required=True)
    #forms.SelectDateWidget()

