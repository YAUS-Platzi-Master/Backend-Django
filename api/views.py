"""Views for API """

#Utilities rest
from rest_framework import viewsets


#Utilities for custom  auth token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#Permisions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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
                                        user_id__user__username=username,
                                        user_id__user__id=pk
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
                                    set_url_id__user_id__user__username=username,
                                    set_url_id__user_id__user__id=pk
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


class SetUrlViewSet(viewsets.ModelViewSet):
    """ Api Endpoint for set of Url"""
    queryset = SetUrl.objects.all()
    serializer_class = SetUrlSerializer




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
