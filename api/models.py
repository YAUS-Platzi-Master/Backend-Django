"""Models for the api urls"""

#Django
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """model for the user Profile
    
    Proxy model that extends the base data
    """
    #Extends model user
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique = True)
    
    #Extra data for user Profile
    phone_number = models.CharField(max_length=20,null=True,blank=False, unique=True)
    modified = models.DateTimeField(auto_now=True)
    
    def  __str__(self):
        """return username"""
        return self.user.username


class SetUrl(models.Model):
    """model for the information that relates short and log URL"""    
    #Id of user
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE, default='')
    
    #Set of urls
    long_url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=50, null=True, unique = True)
    
    #Timestamps
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now_add=True)
    
    #Status
    status = models.CharField(max_length=45)
    
    class Meta:
        ordering = ('-created',)


    def __str__(self):
        """return long url"""
        return self.short_url

class Hit(models.Model):
    """model for hits of a set Url"""

    #Id of set url
    set_url_id = models.ForeignKey("SetUrl", on_delete=models.CASCADE)
    
    #Data from the excecution of shor_url
    http_reffer = models.CharField(max_length=100)
    ip = models.CharField(max_length=45)
    country_code = models.CharField(max_length=2)
    region_code =  models.CharField(max_length=2)
    city = models.CharField(max_length=200)
    lattitude = models.CharField(max_length=45)
    longitude  =  models.CharField(max_length=45)
    agent_client = models.CharField(max_length=45)

    #timestamps
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        """return http_reffer"""
        return self.http_reffer
