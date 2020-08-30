"""App URLs Configuration"""

#Utillities
from django.urls import include, path
from rest_framework import routers

#Views from app urls
from api import views

router = routers.DefaultRouter()
router.register(r'set_of_urls', views.SetUrlViewSet,basename='set_of_urls')
router.register(r'hits', views.HitViewset,basename='hits')

urlpatterns = [
    path('register/new_url',views.RegisterNewUrlView.as_view()),
    path('register/user',views.RegisterUserView.as_view()),
    path('user/', views.UserViewSet.as_view()),
    path('user/hits', views.UserHitsViewSet.as_view()),
    path('', include(router.urls)),
]