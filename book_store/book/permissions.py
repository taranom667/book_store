from rest_framework import permissions
class ShowUserBooksPermission(permissions.BasePermission):
  def has_permission(self, request, view):
      pass