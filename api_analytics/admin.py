"""api analytics classes"""

#utilities
from django.contrib import admin

#Models
from .models import ApiAnalytics

@admin.register(ApiAnalytics)
class ApiAnalyticsAdmin(admin.ModelAdmin):
    """admin profile for api analytics"""

    ist_display = ('id', 'requested_at', 'response_ms', 'status_code',
                    'user_id', 'method',
                    'path', 'remote_addr', 'host',
                    'query_params')
    list_filter = ('method', 'status_code')
    search_fields = ('path', 'user__email',)
    raw_id_fields = ('user_id', )