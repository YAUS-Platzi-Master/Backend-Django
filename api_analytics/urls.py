""" Ulrs for api_analytics app"""

#Utilities
from django.urls import path

#Knox Views
from api_analytics.views import ApiAnalyticsViewSet

urlpatterns = [
    path('', ApiAnalyticsViewSet.as_view()),
] 