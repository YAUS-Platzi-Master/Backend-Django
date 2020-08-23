"""Serializers for models in Api app"""
#Djangorest-framework
from rest_framework import serializers

#Models
from .models import SetUrl, Hit, UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model UserProfile"""
    class Meta:
        model = UserProfile
        fields = [
            #'user',
            'phone_number',
        ]


class SetUrlSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model SetUrl"""
    hits = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='hit-detail'
    )

    class Meta:
        model = SetUrl
        fields = [
            'long_url',
            'short_url',
            'status',
            'hits',
            ]

 
class HitSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model Hit"""
        
    class Meta:
        model = Hit
        fields = [
            'http_reffer',
            'ip',
            'country_code',
            'region_code',
            'city',
            'lattitude',
            'longitude',
            'agent_client',
        ]