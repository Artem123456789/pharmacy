from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == "create":
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if view.action != "create":
            return obj.user == request.user
        return True
