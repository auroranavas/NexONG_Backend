from rest_framework.routers import DefaultRouter
from .Authentication.views import *
from .Event.views import MeetingApiViewSet


router_api = DefaultRouter()
router_api.register(prefix='user', viewset=UserApiViewSet, basename='user')
router_api.register(prefix='event', viewset=MeetingApiViewSet, basename='event')