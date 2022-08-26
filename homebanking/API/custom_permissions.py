
from rest_framework import permissions
from django.contrib.auth.models import User


class AuthenticatedEmployee(permissions.BasePermission):
    
    """
    Permission check for group users.
    """
    

    def has_permission(self, request, view):
        "Needs to return a boolean"
        
        return User.objects.filter(pk = request.user.id, groups__name = 'Empleado').exists()
    
    
class AuthenticatedClient(permissions.BasePermission):
    
    """
    Permission check for group users.
    """
    
    
    def has_permission(self, request, view):
        
        return User.objects.filter(pk = request.user.id, groups__name = 'Cliente').exists()