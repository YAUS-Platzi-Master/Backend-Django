"""Serializers for models in authKnox app"""
#Djangorest-framework
from rest_framework import serializers

#model
from knox.models import AuthToken
from authKnox.models import TokenProfile

class ListTokenSerializer(serializers.ModelSerializer):
    """serializer for list of tokkens"""
    token_profile = serializers.StringRelatedField(many=False)   
    
    class Meta:
        model = AuthToken
        fields = [
                'user',
                'token_key',
                'created',
                'expiry',
                'token_profile',
                ]