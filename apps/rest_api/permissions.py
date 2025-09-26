from rest_framework.permissions import BasePermission

class AllowAnyAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user is None and request.auth is not None  # Authenticated via API key