from rest_framework import permissions

from users.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    """ """
    message = ""
    def has_permission(self, request, view):
        if request.user.role in [User.STATUS.get("admin"),User.STATUS.get("moderator")]:
            return True
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    Разрешение на уровне объекта, чтобы разрешить его редактирование только
    владельцам объекта. Предполагается, что экземпляр модели имеет атрибут «владелец».
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author == request.user