"""Serializers for models in Api app"""
#Djangorest-framework
from rest_framework import serializers

#model
from knox.models import AuthToken

class ListTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = [
                'user',
                'token_key',
                'created',
                'expiry',
                ]