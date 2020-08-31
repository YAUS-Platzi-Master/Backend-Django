"""serializer for ApiAnalytics model"""
#Djangorest-framework
from rest_framework import serializers

#Models
from api_analytics.models import ApiAnalytics


class ApiAnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiAnalytics
        fields = '__all__'


