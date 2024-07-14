from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    message = 'Изменение/удаление чужих данных запрещено.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
