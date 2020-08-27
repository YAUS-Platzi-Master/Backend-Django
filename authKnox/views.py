from django.shortcuts import render

#utilities djjango
from django.contrib.auth import logout, login
#Utilities django rest
from rest_framework.response import Response


#Permisions
from rest_framework.permissions import AllowAny, IsAuthenticated

#django rest knox
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView, LogoutView, LogoutAllView
# from knox.auth import TokenAuthentication




class LoginView(LoginView):
    permission_classes = [AllowAny,]

    def post (self, request, format=None):
        serializer = AuthTokenSerializer(data= request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        login(request, user)

        return super(LoginView,self).post(request,format=None)


class LogoutView(LogoutView):
    permission_classes = [IsAuthenticated,]
    pass


class LogoutAllView(LogoutAllView):
    permission_classes = [IsAuthenticated,]

    pass