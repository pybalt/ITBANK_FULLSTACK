from django.contrib import admin

# Register your models here.

from .models import Prestamo
# Register your models here.


class prestamoAdmin (admin.ModelAdmin):
    readonly_fields= ('created-at','updated-at')
    admin.site.register(Prestamo)