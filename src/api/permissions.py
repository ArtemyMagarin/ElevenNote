from rest_framework import permissions

class IsActive(permissions.BasePermission):
    """
    Check for active user
    """

    def has_permission(self, request, view):

        return request.user.is_active