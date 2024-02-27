from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from ...models import *
from .authSerializer import *


def check_user_is_admin(request):
    user = request.user
    return user.is_staff


def check_user_is_authenticated(request):
    user = request.user
    return user.is_authenticated


class UserApiViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
