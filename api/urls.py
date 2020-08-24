"""App URLs Configuration"""

#Utillities
from django.urls import include, path
from rest_framework import routers

#Views from app urls
from api import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'userProfile', views.UserProfileViewSet)
router.register(r'set_of_urls', views.SetUrlViewSet)
router.register(r'hit', views.HitViewset)

urlpatterns = [
    path('', include(router.urls)),
]
