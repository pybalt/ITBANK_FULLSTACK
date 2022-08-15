from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SolicitudPrestamoForm
from .models import Prestamo
def prestamos(request):
    form_prestamo = SolicitudPrestamoForm()
    if request.method == "POST":
        if form_prestamo.is_valid():
            name = request.POST.get('Nombres','')
            surname = request.POST.get('Apellidos','')
        return redirect(reverse('prestamos')+ "?ok")    
    return render(request, "prestamos/prestamos.html",
    {'form':form_prestamo})
# Create your views here.
