from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow User to Edit Their own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their Own Profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
