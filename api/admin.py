"""User admin classes"""

#django utilities
from django.contrib import admin

#Models in api
from .models import UserProfile,  SetUrl, Hit



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Profile UserProfile"""

    list_display = ('pk','user','phone_number','Is_developer')
    list_display_links = ('pk','user')
    
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'user__date_joined',
        'modified',
    )

@admin.register(SetUrl)
class SetUrlAdmin(admin.ModelAdmin):
    """Profile for setUrl"""
    list_display = (
        'pk',
        'user_id',
        'long_url',
        'short_url',
        'created',
        'deleted'
    )

    list_display_links = ('pk','user_id')
    
    search_fields = (
        'long_url',
        'short_url',
    )

    list_filter = (
        'long_url',
        'short_url',
    )

@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    """Profile for Hit"""
    list_display = (
        'pk',
        'set_url_id',
        'http_reffer',
        'ip',
        'country_code',
        'region_code',
        'city',
        'latitude',
        'longitude',
        'agent_client',
        'created',
    )

    list_display_links = (
        'pk',
        'set_url_id')
    
    search_fields = (
        'http_reffer',
        'ip',
        'city'
    )

    list_filter = (
        'http_reffer',
        'ip',
        'city'
    )
