from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from webitbank.models import Usuario


class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'usuario'

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)