"""Models for the authKnox urls"""

#Django
from django.db import models

#model token
# from knox.models import AuthToken

# class TokenProfile(models.Model):
#     """model for the token Profile
    
#     model that extends the knox_authtoken model
#     """
#     #Extends model user
#     authToken = models.OneToOneField(AuthToken, related_name='token_profile', on_delete=models.CASCADE,unique = True)
    
#     #Extra data for user Profile
#     name_token = models.CharField(max_length=100,null=False)
    
#     class Meta:
#         ordering = ('name_token',)

#     def  __str__(self):
#         """return username"""
#         return f'{self.name_token} : {self.authToken.primary_key}'