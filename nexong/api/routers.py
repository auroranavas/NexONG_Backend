from rest_framework.routers import DefaultRouter
from .Authentication.views import *
from .Meeting.views import *
from .Event.views import *
from .Lesson.views import *

router_api = DefaultRouter()
router_api.register(prefix="user", viewset=UserApiViewSet, basename="user")
router_api.register(prefix="meeting", viewset=MeetingApiViewSet, basename="meeting")
router_api.register(prefix="event", viewset=EventApiViewSet, basename="event")
<<<<<<< HEAD
router_api.register(prefix="lesson", viewset=LessonApiViewSet, basename="lesson")
router_api.register(
    prefix="lessonAttendance",
    viewset=LessonAttendanceApiViewSet,
    basename="lessonAttendance",
)
=======
router_api.register(prefix="volunteer", viewset=EventApiViewSet, basename="volunteer")
>>>>>>> 24385032f91481a1a72476739469f6986db4392f
router_api.register(
    prefix="lesson-event", viewset=LessonEventApiViewSet, basename="lessonevent"
)
