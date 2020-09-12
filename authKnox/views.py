"""views for authknox app"""
from django.shortcuts import render

#utilities djjango
from django.contrib.auth import logout, login
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone

#Decorators
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

#Utilities django rest
from rest_framework.response import Response
from rest_framework import status

#Permisions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

#django rest knox
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView, LogoutView, LogoutAllView
# from knox.auth import TokenAuthentication

#Utilities rest
from rest_framework import generics
from rest_framework.views import APIView

# #Serializer
from authKnox.serializers import ListTokenSerializer, TokenProfile

#model
from knox.models import AuthToken
from authKnox.models import TokenProfile
from django.contrib.auth.models import User

#throttle
from api.throttles import AnonLoginUrlThrottle

#API Analytics
from api_analytics.mixins import LoggingMixin    

class ListTokenProfileView(LoggingMixin,APIView):
    """ List all token for the authenticated user"""

    permission_classes = [IsAuthenticated]
    serializer_class = ListTokenSerializer
    
    def get(self,request, format=None):
        """Get alll tokens for the authenticated user"""
        username = self.request.user.username
        
        queryset = AuthToken.objects.filter(user__username=username)
        
        serializer = ListTokenSerializer(queryset,many =True)
        data={}
        data['username']=username
        data['count']= queryset.count()
        data['tokens']=serializer.data
        return Response(data=data,status=status.HTTP_200_OK)


@method_decorator(csrf_exempt,name='post')
class LoginView(LoggingMixin,LoginView):
    """Login View"""
    permission_classes = [AllowAny]
    throttle_classes  = [AnonLoginUrlThrottle]


    def post(self, request, format=None):
        """Post a Login"""
        serializer = AuthTokenSerializer(data= request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        login(request, user)

        token_limit_per_user = self.get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            token = request.user.auth_token_set.filter(expiry__gt=now)
            if token.count() >= token_limit_per_user:
                return Response(
                    {"error": "Maximum amount of tokens allowed per user exceeded."},
                    status=status.HTTP_403_FORBIDDEN
                )
        
        token_ttl = self.get_token_ttl()
        
        instance, token = AuthToken.objects.create(request.user, token_ttl)
        
        user_logged_in.send(
            sender=request.user.__class__,
            request=request, 
            user=request.user
        )

        #Set the information of user for identify the source of token
        token_profile = TokenProfile(
            token=instance,
            user_agent= request.headers.get('user-agent'),
            Host=request.headers.get('host'),
            name_token=request.headers.get('name_token'),                  
        )

        token_profile.save()
        data = self.get_post_response_data(request, token, instance,token_profile)
        
        return Response(data=data,status=status.HTTP_201_CREATED)


    def get_post_response_data(self, request, token, instance,token_profile):
        """ Resolve the response to login"""
        UserSerializer = self.get_user_serializer_class()

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data

        data['token_profile'] = {
            'name_token':token_profile.name_token,
            'user_agent':token_profile.user_agent,
            'Host':token_profile.Host,                            
        }

        return data


class LogoutView(LoggingMixin,LogoutView):
    """logout all view"""
    permission_classes = [IsAuthenticated,]
    
    def post(self, request, format=None):
        """post a logout all"""
        request._auth.delete()
        user_logged_out.send(
            sender=request.user.__class__,
            request=request, 
            user=request.user
        )
        
        data = {}
        data['Response'] = 'Logout Succesfully'
        data['Number_Logout'] = 'one'
        data['User']= request.user.username
        
        
        return Response(data=data,status=status.HTTP_200_OK)


class LogoutAllView(LoggingMixin,LogoutAllView):
    """logout all view"""
    permission_classes = [IsAuthenticated,]

    def post(self, request, format=None):
        """post a logout all"""
        data_source = request.headers
        request.user.auth_token_set.all().delete()
        user_logged_out.send(
            sender=request.user.__class__,
            request=request, 
            user=request.user
        )

        data = {}
        data['Response'] = 'Logout Succesfully'
        data['Number_Logout'] = 'all'
        data['User']= request.user.username 
        
        return Response(data=data, status=status.HTTP_200_OK)