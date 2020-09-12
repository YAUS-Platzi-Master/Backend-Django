"""Models for the authKnox urls"""

#Django
from django.db import models

#model token
from knox.models import AuthToken

class TokenProfile(models.Model):
    """model for the token Profile
    
    model that extends the knox_authtoken model
    """
    #Extends model user
    token = models.OneToOneField(AuthToken, related_name='token_profile', on_delete=models.CASCADE,unique = True)
    
    #Extra data for user Profile
    user_agent = models.CharField(max_length=1000,null=True)
    Host = models.CharField(max_length=100,null=True)
    Cookie = models.CharField(max_length=1000,null=True)

    class Meta:
        ordering = ('Host',)

    def  __str__(self):
        """return username"""
        return f' {self.Host} : {self.user_agent}'