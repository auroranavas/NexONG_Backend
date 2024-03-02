from nexong.api.Event.views import EventApiViewSet
from rest_framework.routers import DefaultRouter
from .Authentication.views import *
from .Meeting.views import *
from .Event.views import *

router_api = DefaultRouter()
router_api.register(prefix="user", viewset=UserApiViewSet, basename="user")
router_api.register(prefix="meeting", viewset=MeetingApiViewSet, basename="meeting")
router_api.register(prefix="event", viewset=EventApiViewSet, basename="event")
router_api.register(prefix="educator", viewset=EducatorGetApiViewSet, basename="educator")
router_api.register(prefix="partner", viewset=PartnerGetApiViewSet, basename="partner")
router_api.register(prefix="volunteer", viewset=VolunteerGetApiViewSet, basename="volunteer")
router_api.register(prefix="family", viewset=FamilyGetApiViewSet, basename="family")
router_api.register(prefix="lesson-event", viewset=LessonEventApiViewSet, basename="lessonevent")

