"""" main urls configuration"""

#Utilities
from django.urls import path, include
from django.contrib import admin

#Urls from api app
from api import urls

#Utilities Rest-framework
from api.views  import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/', include(urls)),
    path('api-token-auth/',CustomAuthToken.as_view())

]