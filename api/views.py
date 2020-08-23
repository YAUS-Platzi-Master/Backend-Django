"""Views for API """

#Utilities
from rest_framework import viewsets

#Models
from .models import  UserProfile, SetUrl, Hit

#Django model
from django.contrib.auth.models import User

#Serializers
from .serializers import UserSerializer, UserProfileSerializer, SetUrlSerializer, HitSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for UserProfile"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class SetUrlViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for set of Url"""
    queryset = SetUrl.objects.all()
    serializer_class = SetUrlSerializer
    
class HitViewset(viewsets.ModelViewSet):
    """ Api Endpoint for hit of setUrl"""
    queryset = Hit.objects.all()
    serializer_class = HitSerializer