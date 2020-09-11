
"""View for API Analytics"""

#Utilities DRF
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

#Serializer
from api_analytics.serializers import ApiAnalyticsSerializer

#model
from api_analytics.models import ApiAnalytics

#Api Analitics
from api_analytics.mixins import LoggingMixin

class ApiAnalyticsViewSet(viewsets.ModelViewSet):
    """ Api Endpoint logs in API"""
    permission_classes = [IsAdminUser]
    serializer_class = ApiAnalyticsSerializer
    
    def get_queryset(self):
        return ApiAnalytics.objects.all()
    
    def list(self, request):
        """Returns all logs in API"""

        queryset = self.get_queryset()
        
        #serialize the data        
        serializer = ApiAnalyticsSerializer(queryset,many=True)
        
        #making the response
        data = {}
        # data['Response'] = 'Sets of Urls for user'
        # data['user'] = self.request.user.username
        # data['set_urls_per_user']= queryset.count()
        data['data'] = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)