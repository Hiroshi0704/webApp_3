from rest_framework.permissions import BasePermission


class IsShiftAppOwner(BasePermission):
    message = 'Access denied. "ShiftApp" owner can edit it.'

    def has_object_permission(self, request, view, obj):
        return obj.app.user == request.user


class IsOwner(BasePermission):
    message = 'Access denied. Only owner can edit it.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
