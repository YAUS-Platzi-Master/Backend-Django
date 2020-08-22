"""Serializers for models in Api app"""
#Djangorest-frameword
from rest_framework import serializers

#Models
from .models import SetUrl, Hit, UserProfile


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model UserProfile"""
    class Meta:
        model = UserProfile
        fields = '__all__'

class SetUrlSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model SetUrl"""
    class Meta:
        model = SetUrl
        fields = '__all__'

class HitSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model Hit"""
    class Meta:
        model = Hit
        fields = '__all__'