""" Ulrs for auth app"""

#Utilities
from django.urls import path, include

#Knox Views
from authKnox.views import LoginView,LogoutView, LogoutAllView
from authKnox.views import ListTokenProfileView



urlpatterns = [
    path('login/', LoginView.as_view(), name = 'knox_login' ),
    path('logout/', LogoutView.as_view(), name = 'knox_logout' ),
    path('logout_all/', LogoutAllView.as_view(), name = 'knox_logout_all' ),
    path('list_token/', ListTokenProfileView.as_view(), name = 'list_token' ),
] 