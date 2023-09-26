from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsOwnerOrReadOnly(BasePermission):
    message = 'Permissions is denied, You are not owner This Note'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user