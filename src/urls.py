from django.contrib import admin
from django.urls import path, include
from nexong.api.routers import router_api
from nexong.api.Authentication.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router_api.urls)),
    path('api/educator', EducatorCApiViewSet.as_view()),
    path('api/educator/<int:id>', EducatorUDApiViewSet.as_view()),
    path('api/volunteer', EducatorCApiViewSet.as_view()),
    path('api/volunteer/<int:id>', EducatorUDApiViewSet.as_view()),
    path('api/partner', EducatorCApiViewSet.as_view()),
    path('api/partner/<int:id>', EducatorUDApiViewSet.as_view()),
    path('api/family', EducatorCApiViewSet.as_view()),
    path('api/family/<int:id>', EducatorUDApiViewSet.as_view()),
    path('api/educationCenter', EducatorCApiViewSet.as_view()),
    path('api/educationCenter/<int:id>', EducatorUDApiViewSet.as_view()),
]
