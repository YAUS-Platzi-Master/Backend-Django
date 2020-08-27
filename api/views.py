"""Views for API """

#Utilities rest
from rest_framework import viewsets, generics


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
            data['Response'] = 'User created succesfully'
            data['username'] = user.username
            data['email'] = user.email
        else:
            
            data = serializer.errors
            data['Response'] = 'Error user dont created'
        return Response(data)



class RegisterNewUrlView(generics.CreateAPIView):
    """Register a new shor url"""
    permission_classes = [AllowAny]
    serializer_class = SetUrlSerializer

    def create(self, request, *args, **kwargs):
        #register a new set of urls

        request.data['status'] = 'Active'
        serializer = SetUrlSerializer(data=self.request.data)
        
        data = {}

        if serializer.is_valid(): #check if the params are valid
            new_set_url = SetUrl(
                    long_url=serializer.data['long_url'],
                    status = serializer.data['status']
            )
            
            
            if request.auth: #check if is authenticated user
                new_set_url.user_id = request.user
                
                if request.data['custom_url']: #check if authenticated user wants a custom url
                    
                    if 'short_url_custom' in request.data:
                        new_set_url.short_url = request.data['short_url_custom']
                        data['Response'] = 'Register new custom url for authenticated User'
                    
                    else:
                        data['Response'] = 'Not register. Must pass a short_url_custom'
                        return Response(data,status=200) 

                else:  
                    new_set_url.short_url = token_urlsafe(nbytes=5)
                    data['Response'] = 'Register new random url for authenticated User'

            else: 
                
                if not request.data['custom_url']:
                    new_set_url.short_url = token_urlsafe(nbytes=5)
                    data['Response'] = 'Register new random url for anonymous user'

                else:
                    data['Response'] = 'custom url no avaliable for anonymous user'
                    return Response(data,status=200)  
            
        
            new_set_url.save()
            data['register_set'] = SetUrlSerializer(new_set_url).data
        
        else: 
            data = serializer.error_messages
            data['Response'] = 'Format of params invalid'
        
        return Response(data,status=200)

    

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    @action(methods=['get'], detail=True,permission_classes = [IsAuthenticated])
    def details(self, request, pk=None):
        """Returns only the info for the user authenticated"""

        #Take the username from the request
        username = self.request.user.username

        #filter the queriset by the username
        queryset = self.get_queryset().filter(
                                        username=username,
                                        id=pk
                                        )

        #serialize the data        
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True,permission_classes = [IsAuthenticated])
    def set_urls(self, request, pk=None):
        """Returns only the set_urls for the user authenticated"""
    
        #Take the username from the request
        username = self.request.user.username
        
        #filter the queryset by the username authenticated
        queryset = SetUrl.objects.filter(
                                        user_id__username=username,
                                        user_id__id=pk
                                        )

        #serialize the data        
        serializer = SetUrlSerializer(queryset,many=True)
        
        return Response({
                            'total_set_urls': queryset.count(),
                            'data': serializer.data,
        })

    @action(methods=['get'], detail=True,permission_classes = [IsAuthenticated])
    def hits(self, request, pk=None):
        """Returns only the info for the user authenticated"""

        #Take the username from the request
        username = self.request.user.username

        #queryset = Hit.objects.filter(set_url_id=3)
        queryset = Hit.objects.filter(
                                    set_url_id__user_id__username=username,
                                    set_url_id__user_id__id=pk
                                    )
        
        #serialize the data        
        serializer = HitSerializer(queryset,many=True)
        
        return Response({
                            'total_hits':queryset.count(),
                            'data':serializer.data,
                        })



class UserProfileViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for UserProfile"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]


class SetUrlViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for set of Url"""
    queryset = SetUrl.objects.all()
    serializer_class = SetUrlSerializer
    permission_classes = [IsAuthenticated]


    @action(methods=['get'], detail=True,)
    def hits(self, request, pk=None):
        queryset = SetUrl.objects.filter(hits=request.SetUrl_id)



class HitViewset(viewsets.ModelViewSet):
    """ Api Endpoint for hit of hit"""
    queryset = Hit.objects.all()
    serializer_class = HitSerializer


class CustomAuthToken(ObtainAuthToken):
    """ Api endpoint for create a custom token
    
    Takes the base class ObtainAuthToken and add some things"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
                                            data=request.data,
                                            context={'request': request}
                                            )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })
