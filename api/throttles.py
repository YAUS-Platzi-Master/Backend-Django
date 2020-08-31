"""throttling custom model"""

#rest frameword utilities
from rest_framework import  throttling
from django.core.exceptions import ImproperlyConfigured

#model for queryset
from api.models import UserProfile

#serializer
from api.serializers import UserProfileSerializer

class AnonLoginUrlThrottle(throttling.AnonRateThrottle):
    scope = 'anon_login'


class AnonRegisterUrlThrottle(throttling.AnonRateThrottle):
    scope = 'anon_register_url'

class UserRegisterUrlThrottle(throttling.UserRateThrottle):
    scope = 'user'

    def resolve_scope(self,request):
        
        if request.user.is_anonymous:
            return 'user'

                
        queryset = UserProfile.objects.filter(user=request.user,Is_developer=True)
        serializer_class = UserProfileSerializer(data=queryset,many=True)
        serializer_class.is_valid()
        
        if serializer_class.data:
            scope = 'developer_register_url'
        else: 
            scope = 'common_register_url'

        return scope

    def allow_request(self, request, view):
        # We can only determine the scope once we're called by the view.
        self.scope = self.resolve_scope(request)
        
        # If a view does not have a `throttle_scope` always allow the request
        if not self.scope:
            return True

        # Determine the allowed request rate as we normally would during
        # the `__init__` call.
        self.rate = self.get_rate()
        self.num_requests, self.duration = self.parse_rate(self.rate)

        # We can now proceed as normal.
        return super().allow_request(request, view)