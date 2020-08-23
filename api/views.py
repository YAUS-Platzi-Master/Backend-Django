"""Views for API """

#Utilities
from rest_framework import viewsets

#Models
from .models import  UserProfile, SetUrl, Hit

#Serializers
from .serializers import UserProfileSerializer, SetUrlSerializer, HitSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for UserProfile"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class SetUrlViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for set of Url"""
    queryset = SetUrl.objects.all()
    serializer_class = SetUrlSerializer
    
    def create(self, request,*args, **kwargs):
            pass
    
class HitViewset(viewsets.ModelViewSet):
    """ Api Endpoint for hit of setUrl"""
    queryset = Hit.objects.all()
    serializer_class = HitSerializer


