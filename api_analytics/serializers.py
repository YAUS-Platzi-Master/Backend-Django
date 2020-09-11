"""serializer for ApiAnalytics model"""
#Djangorest-framework
from rest_framework import serializers

#Models
from api_analytics.models import ApiAnalytics


class ApiAnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiAnalytics
        fields = [
            'id', 
            'requested_at', 
            'response_ms', 
            'status_code',
            'user_id', 
            'method',
            'path', 
            'remote_addr', 
            'host',
            'query_params'
        ]


