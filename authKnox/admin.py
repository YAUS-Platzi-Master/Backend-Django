from django.contrib import admin

#model
from authKnox.models import TokenProfile



@admin.register(TokenProfile)
class TokenProfileAdmin(admin.ModelAdmin):
    """Profile UserProfile"""

    list_display = ('pk','user_agent', 'Host',  'Cookie')
    list_display_links = ('pk',)
    
    search_fields = (
        'pk',
        'user_agent',
        'Host',
        'Cookie',
    )

    list_filter = (
        'user_agent',
        'Host',
        'Cookie',
    )