"""Models for the api urls"""

#Django
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """model for the user Profile
    
    model that extends the base data
    """
    #Extends model user
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE,unique = True)
    
    #Extra data for user Profile
    phone_number = models.CharField(max_length=20,null=True,blank=False, unique=True)
    Is_developer = models.BooleanField(verbose_name='Is_developer',default=False, null=True)
    modified = models.DateTimeField(auto_now=True)
    
    def  __str__(self):
        """return username"""
        return f'{self.Is_developer}'


class SetUrl(models.Model):
    """model for the information that relates short and log URL"""    
    #Id of user
    user_id = models.ForeignKey(User, related_name= 'set_url',on_delete=models.CASCADE, default=None,null=True)
    
    #Set of urls
    long_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=50, null=True, unique = True)
    
    #Timestamps
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(default=None,null=True)
    
    #Status
    status = models.CharField(max_length=45)
    
    class Meta:
        ordering = ('-created',)


    def __str__(self):
        """return long url"""
        return f'User: {self.user_id} | Short url: {self.short_url}'

class Hit(models.Model):
    """model for hits of a set Url"""

    #Id of set url
    set_url_id = models.ForeignKey(SetUrl,related_name = 'hits', on_delete=models.CASCADE)
    
    #Data from the excecution of shor_url
    http_reffer = models.CharField(max_length=100, null = True)
    ip = models.CharField(max_length=45, null = True)
    country_code = models.CharField(max_length=2, null = True)
    region_code =  models.CharField(max_length=2, null = True)
    city = models.CharField(max_length=200, null = True)
    latitude = models.CharField(max_length=45, null = True)
    longitude  =  models.CharField(max_length=45, null = True)
    agent_client = models.CharField(max_length=45, null = True)

    #timestamps
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        """return urls hitted"""
        return f'set url: {self.set_url_id.short_url} | Http_refer: {self.http_reffer}'
