from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status
from ...models import *
from .authSerializer import *
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


def check_user_is_admin(request):
    user = request.user
    return user.is_staff


def check_user_is_authenticated(request):
    user = request.user
    return user.is_authenticated


def process_instance(serializer_class, instance, data):
    serializer = serializer_class(instance, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApiViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class EducatorGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = EducatorGetSerializer
    queryset = Educator.objects.all()


class EducatorCApiViewSet(APIView):
    http_method_names = ["post"]
    serializer_class = EducatorSerializer

    def post(self, request):
        serializer = EducatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EducatorUDApiViewSet(APIView):
    http_method_names = ["put", "delete"]
    serializer_class = EducatorSerializer

    def put(self, request, id):
        try:
            educator = Educator.objects.get(pk=id)
        except Educator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return process_instance(EducatorSerializer, educator, request.data)

    def delete(self, request, id):
        try:
            educator = Educator.objects.get(pk=id)

        except Educator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        educator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PartnerGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = PartnerGetSerializer
    queryset = Partner.objects.all()


class PartnerCApiViewSet(APIView):
    http_method_names = ["post"]
    serializer_class = PartnerSerializer

    def post(self, request):
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PartnerUDApiViewSet(APIView):
    serializer_class = PartnerSerializer

    def put(self, request, id):
        try:
            partner = Partner.objects.get(pk=id)
        except Partner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return process_instance(PartnerSerializer, partner, request.data)

    def delete(self, request, id):
        try:
            partner = Partner.objects.get(pk=id)
        except Partner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        partner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VolunteerGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = VolunteerGetSerializer
    queryset = Volunteer.objects.all()


class VolunteerCApiViewSet(APIView):
    http_method_names = ["post"]
    serializer_class = VolunteerSerializer

    def post(self, request):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VolunteerUDApiViewSet(APIView):
    serializer_class = VolunteerSerializer

    def put(self, request, id):
        try:
            volunteer = Volunteer.objects.get(pk=id)
        except Volunteer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return process_instance(VolunteerSerializer, volunteer, request.data)

    def delete(self, request, id):
        try:
            volunteer = Volunteer.objects.get(pk=id)
        except Volunteer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        volunteer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FamilyGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = FamilyGetSerializer
    queryset = Family.objects.all()


class FamilyCApiViewSet(APIView):
    http_method_names = ["post"]
    serializer_class = FamilySerializer

    def post(self, request):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FamilyUDApiViewSet(APIView):
    serializer_class = FamilySerializer

    def put(self, request, id):
        try:
            family = Family.objects.get(pk=id)
        except Family.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return process_instance(FamilySerializer, family, request.data)

    def delete(self, request):
        try:
            family = Family.objects.get(pk=request.data["id"])
        except Family.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        family.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EducationCenterGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = EducationCenterGetSerializer
    queryset = EducationCenter.objects.all()


class EducationCenterCApiViewSet(APIView):
    http_method_names = ["post"]
    serializer_class = EducationCenterSerializer

    def post(self, request):
        serializer = EducationCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EducationCenterUDApiViewSet(APIView):
    serializer_class = EducationCenterSerializer

    def put(self, request, id):
        try:
            educationCenter = EducationCenter.objects.get(pk=id)
        except EducationCenter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return process_instance(
            EducationCenterSerializer, educationCenter, request.data
        )

    def delete(self, request, id):
        try:
            educationCenter = EducationCenter.objects.get(pk=id)
        except EducationCenter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        educationCenter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
