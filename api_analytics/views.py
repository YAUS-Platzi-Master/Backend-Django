
"""View for API Analytics"""

#Utilities DRF
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

#Serializer
from api_analytics.serializers import ApiAnalyticsSerializer

#model
from api_analytics.models import ApiAnalytics

class ApiAnalyticsViewSet(generics.ListAPIView):
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
        data['Response'] = 'Logs in API'
        data['user'] = self.request.user.username
        data['total_logs']= queryset.count()
        data['data'] = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)

    