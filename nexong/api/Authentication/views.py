from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from ...models import *
from .authSerializer import *

class UserApiViewSet(ModelViewSet):
    http_method_names = ['get','post']
    serializer_class = UserSerializer
    queryset = User.objects.all()