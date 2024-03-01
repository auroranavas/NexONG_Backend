from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from ...models import *
from .authSerializer import *
from rest_framework.views import APIView


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


class EducatorGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = EducatorGetSerializer
    queryset = Educator.objects.all()

class EducatorCUDApiViewSet(APIView):
    http_method_names = ["post", "put", "delete"]
    serializer_class = EducatorSerializer
    
    def post(self, request, format = None):
        serializer = EducatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, format = None):
            try:
                educator = Educator.objects.get(pk=request.data['id'])
            except Educator.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = EducatorSerializer(educator, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format = None):
        
        try:
            educator = Educator.objects.get(pk=request.data['id'])  

        except Educator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        educator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PartnerGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = PartnerGetSerializer
    queryset = Partner.objects.all()

class PartnerCUDApiViewSet(APIView):
    http_method_names = ['post', 'put', 'delete']
    serializer_class = PartnerSerializer
    
    def post(self, request, format = None):
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, format = None):
            try:
                partner = Partner.objects.get(pk=request.data['id'])
            except Partner.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = PartnerSerializer(partner, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format = None):
       
        try:
            partner = Partner.objects.get(pk=request.data['id'])
        except Partner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        partner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VolunteerGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = VolunteerGetSerializer
    queryset = Volunteer.objects.all()

class VolunteerCUDApiViewSet(APIView):
    http_method_names = ['post', 'put', 'delete']
    serializer_class = VolunteerSerializer
    
    def post(self, request, format = None):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, format = None):
            try:
                volunteer = Volunteer.objects.get(pk=request.data['id'])
            except Volunteer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = VolunteerSerializer(volunteer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format = None):
        
        try:
            volunteer = Volunteer.objects.get(pk=request.data['id'])
        except Volunteer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        volunteer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FamilyGetApiViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = FamilyGetSerializer
    queryset = Family.objects.all()

class FamilyCUDApiViewSet(APIView):
    http_method_names = ['post', 'put', 'delete']
    serializer_class = FamilySerializer
    
    def post(self, request, format = None):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, format = None):
            try:
                family = Family.objects.get(pk=request.data['id'])
            except Family.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = FamilySerializer(family, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format = None):
    
        try:
            family = Family.objects.get(pk=request.data['id'])
        except Family.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        family.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)