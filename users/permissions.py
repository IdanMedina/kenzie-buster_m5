from rest_framework import permissions
from rest_framework.views import View, Request
from .models import User


class IsUserEmployee(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User
                              ) -> bool:
        if obj == request.user:
            return True
        return request.user.is_superuser
