from django.contrib import admin
from django.urls import path, include
from nexong.api.routers import router_api
from nexong.api.Authentication.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router_api.urls)),
    path("api/educator", EducatorCUDApiViewSet.as_view()),
    path("api/volunteer", VolunteerCUDApiViewSet.as_view()),
    path("api/partner", PartnerCUDApiViewSet.as_view()),
    path("api/family", FamilyCUDApiViewSet.as_view())
      
      ]
