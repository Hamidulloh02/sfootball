from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsCorrectRoleAndUsername(BasePermission):
    """
    Custom permission to only allow users with a specific role and username to access the view.
    """
    
    def has_permission(self, request, view):
        # Get the user making the request
        user = request.user
        
        # Ensure the user is authenticated
        if not user or not user.is_authenticated:
            return False
        
        # Check if the user's role and username match the required values
        required_role = 'manager'  # Set this to the role you want to allow
        required_username = 'john_doe'  # Set this to the username you want to allow

        if user.role == required_role and user.username == required_username:
            return True
        
        return False