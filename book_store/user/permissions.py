from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class  IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True



class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return True