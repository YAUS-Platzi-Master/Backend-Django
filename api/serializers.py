"""Serializers for models in Api app"""
#Djangorest-framework
from rest_framework import serializers

#Models
from .models import SetUrl, Hit, UserProfile

#Django model
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            # 'is_staff',
            # 'user_profile',
            # 'auth_token',
            'password',
            #'date_joined',
            'id',
            #'is_active',
            #'is_superuser',
            #'last_login'
            
        ]
        extra_kwargs = {
            'password': {'write_only':True},
        }

    def save(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model UserProfile"""
    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
        ]


class SetUrlSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the model SetUrl"""

    class Meta:
        model = SetUrl
        fields = [
            'long_url',
            'short_url',
            'status',
            # 'hits',
            'created',
            #'deleted',
            'id',
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
            'latitude',
            'longitude',
            'agent_client',
            'created',
            'id',
        ]