from email.policy import default
from django import forms
class SolicitudPrestamoForm(forms.Form):
    name = forms.CharField(label= 'Nombres', required=True)
    surname = forms.CharField(label= 'Apellidos', required=True)
    dni= forms.IntegerField(label= 'DNI', required= True)
    startDate = forms.DateField(label = 'Fecha de Inicio', required=True)
    loan_type = forms.ChoiceField(label = 'Tipo de Préstamo', required=True, 
    choices= [
        ('HIPOTECARIO', 'Hipotecario'),
        ('PERSONAL', 'Personal'),
        ('PRENDARIO', 'Prendario'),
    ], default= 'PERSONAL')
    amount = forms.IntegerField(label = 'Monto del Préstamo', required=True) 