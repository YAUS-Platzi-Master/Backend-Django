""" model for api analitics"""

#utilities
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class ApiAnalytics(models.Model):
    """
    Logs Django rest framework API requests 
    """

    user_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    requested_at = models.DateTimeField(auto_now_add=True,db_index=True)
    
    response_ms = models.PositiveIntegerField(default=0)
    
    path = models.CharField(
        max_length=100,
        db_index=True, 
        help_text='url path',
    )

    view = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        db_index=True,
        help_text='method called by this endpoint',
    )

    remote_addr = models.GenericIPAddressField()
    host = models.URLField()
    method = models.CharField(max_length=10)
    query_params = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    errors = models.TextField(null=True, blank=True)
    status_code = models.PositiveIntegerField(null=True, blank=True)
    # objects = PrefetchUserManager()

    class Meta:
        verbose_name = 'API Request Log'

    def __str__(self):
        return '{} {}'.format(self.method, self.path)