"""Views for API """
#python utilites
import re


#Utilities rest
from rest_framework import viewsets, generics
from rest_framework import status

#Utilities for custom  auth token
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#Permisions
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny

#Authentication
from rest_framework.authentication import TokenAuthentication

#routing viewsets
from rest_framework.decorators import action

#Django model
from django.contrib.auth.models import User

#Models
from .models import  UserProfile, SetUrl, Hit

#Serializers
from .serializers import UserSerializer, UserProfileSerializer, SetUrlSerializer, HitSerializer
from django.db.migrations import serializer

#python utilities
from secrets import token_urlsafe

#throttle
from api.throttles import AnonRegisterUrlThrottle, UserRegisterUrlThrottle

class RegisterUserView(generics.CreateAPIView):
    """ Register a new user"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        #register a new user
        serializer = UserSerializer(data=self.request.data)
        data = {}
        if serializer.is_valid():
            #check if the params are valid
            user = serializer.save(validated_data=serializer.validated_data)
            
            #save profile
            profile = UserProfile(user=user,Is_developer=False)
            profile.save()
            #making response
            data['Response'] = 'User created succesfully'
            data['username'] = user.username
            data['email'] = user.email
            data['Is_developer'] = profile.Is_developer
        else:
            
            data = serializer.errors
            data['Response'] = 'Error user dont created'
        return Response(data=data,status=status.HTTP_201_CREATED)
        

class RegisterNewUrlView(generics.CreateAPIView):
    """Register a new shor url"""
    permission_classes = [AllowAny]
    serializer_class = SetUrlSerializer
    throttle_classes = [AnonRegisterUrlThrottle,UserRegisterUrlThrottle]
    
    def create(self, request, *args, **kwargs):
        #register a new set of urls

        request.data['status'] = 'Active'


        patron = re.compile(r'/^\/[a-z0-9\-]+$/i')

        serializer = SetUrlSerializer(data=self.request.data)
        
        data = {}

        if serializer.is_valid(): #check if the params are valid
            new_set_url = SetUrl(
                    long_url=self.request.data['long_url'],
                    status = self.request.data['status']
            )
            
            
            if request.auth: #check if is authenticated user
                new_set_url.user_id = request.user
                
                if request.data['custom_url']: #check if authenticated user wants a custom url
                    
                    if 'short_url_custom' in request.data:

                        if re.search(r'^[a-z0-9-]+$',request.data['short_url_custom']) == None: #check if has the characters allowed
                            data['Response'] = 'short_url_custom invalid. Only accept letters, numbers or guion'
                            return Response(data=data,status=status.HTTP_400_BAD_REQUEST) 

                        else:
                            new_set_url.short_url = request.data['short_url_custom']
                            data['Response'] = 'Register new custom url for authenticated User'
                    
                    else:
                        data['Response'] = 'Not registed. Must pass a short_url_custom'
                        return Response(data=data,status=status.HTTP_401_UNAUTHORIZED) 

                else:  
                    new_set_url.short_url = token_urlsafe(nbytes=5)
                    data['Response'] = 'Register new random url for authenticated User'

            else: 
                
                if not request.data['custom_url']:
                    new_set_url.short_url = token_urlsafe(nbytes=5)
                    data['Response'] = 'Register new random url for anonymous user'

                else:
                    data['Response'] = 'custom url no avaliable for anonymous user'
                    return Response(data=data,status=status.HTTP_400_BAD_REQUEST)  
            
        
            new_set_url.save()
            data['register_set'] = SetUrlSerializer(new_set_url).data
        
        else: 
            data = serializer.error_messages
            data['Response'] = 'Format of params invalid'
        
        return Response(data=data,status=status.HTTP_200_OK)

    

class UserViewSet(generics.ListAPIView):
    """API endpoint for User"""
    
    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)

    def list(self, request, pk=None):
        """Returns only the info for the user authenticated"""

        queryset = self.get_queryset()

        #serialize the data        
        serializer = UserSerializer(queryset,many=True)
        
        #making the response
        data = {}
        data['Response'] = 'User details'
        data['data']=serializer.data

        return Response(data=data,status=status.HTTP_200_OK)

class UserHitsViewSet(generics.ListAPIView):
    """class for read all hits for a user"""
    def get_queryset(self):
        return Hit.objects.filter(set_url_id__user_id__username=self.request.user.username)
        
    def list(self, request, pk=None):
        """Returns only the info for the user authenticated"""
        username = self.request.user.username
        
        queryset = self.get_queryset()

        #serialize the data        
        serializer = HitSerializer(queryset,many=True)
        
        #Making the response
        data = {}
        data['Response'] = 'Hits for user'
        data['user']= self.request.user.username
        data['count'] = queryset.count()
        data['data'] = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class SetUrlViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for set of Url"""
    serializer_class = SetUrlSerializer
    
    def get_queryset(self):
        return SetUrl.objects.filter(user_id__username=self.request.user.username)
    
    def list(self, request, pk=None):
        """Returns only the set_urls for the user authenticated"""

        queryset = self.get_queryset()
        
        #serialize the data        
        serializer = SetUrlSerializer(queryset,many=True,context={'request': request})
        
        #making the response
        data = {}
        data['Response'] = 'Sets of Urls for user'
        data['user'] = self.request.user.username
        data['set_urls_per_user']= queryset.count()
        data['data'] = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)

    

class HitViewset(viewsets.ModelViewSet):
    """ Api Endpoint for hits of users"""
    # queryset = Hit.objects.all()
    serializer_class = HitSerializer

    def get_queryset(self):
        return Hit.objects.filter(set_url_id__user_id__username=self.request.user.username)
        
    def list(self, request, pk=None):
        """Returns only the info for the user authenticated"""
        username = self.request.user.username
        
        queryset = self.get_queryset()

        #serialize the data        
        serializer = HitSerializer(queryset,many=True)
        
        #Making the response
        data = {}
        data['Response'] = 'Hits for user'
        data['user']= self.request.user.username
        data['hits_per_user'] = queryset.count()
        data['data'] = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)