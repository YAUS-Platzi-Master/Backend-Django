"""Serializers for models in Api app"""
#Djangorest-framework
from rest_framework import serializers

#Models
from .models import SetUrl, Hit, UserProfile

#Django model
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # user_profile= serializers.StringRelatedField(many=False)
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
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
    hits = serializers.HyperlinkedRelatedField(
                                                many=True,
                                                read_only=True,
                                                view_name='hits-detail'
                                            )
    
    total_hits = serializers.SerializerMethodField()

    class Meta:
        model = SetUrl
        fields = [
            'id',
            'status',
            'long_url',
            'short_url',
            'created',
            'total_hits',
            'hits',
            ]
    
    def get_total_hits(self,obj):
        return obj.hits.count()


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