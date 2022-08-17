from email.policy import default
from django import forms
class SolicitudPrestamoForm(forms.Form):
    name = forms.CharField(label= 'Nombres', required=True)
    surname = forms.CharField(label= 'Apellidos', required=True)
    dni= forms.CharField(label= 'DNI', required= True)
    startDate = forms.CharField(label = 'Fecha de Inicio', required=True, widget=forms.SelectDateWidget)
    loan_type = forms.ChoiceField(label = 'Tipo de Préstamo', required=True, 
    choices= [
        ('', 'Seleccione una opción'),
        ('HIPOTECARIO', 'Hipotecario'),
        ('PERSONAL', 'Personal'),
        ('PRENDARIO', 'Prendario'),
        ])
    amount = forms.IntegerField(label = 'Monto del Préstamo', required=True) 