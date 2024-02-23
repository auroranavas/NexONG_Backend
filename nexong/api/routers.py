from rest_framework.routers import DefaultRouter
from .Authentication.views import *


router_api = DefaultRouter()
router_api.register(prefix='user', viewset=UserApiViewSet, basename='user')