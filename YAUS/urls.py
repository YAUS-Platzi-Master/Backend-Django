"""" main urls configuration"""

#Utilities
from django.urls import path, include
from django.contrib import admin

#Urls from api app
from api import urls as api_urls

#urls from knox
from authKnox import urls as authKnox_urls
#Utilities Rest-framework
#from api.views  import CustomAuthToken

#Knox Views
from knox import views as knox_views
from authKnox.views import LoginView   


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/', include(api_urls)),
    path('api/auth/', include(authKnox_urls)),

]