"""App URLs Configuration"""

#Utillities
from django.urls import include, path
from rest_framework import routers

#Views from app urls
from api import views

#urls fron api_analytics
from api_analytics import urls as api_analytics_urls

router = routers.DefaultRouter()
router.register(r'set_of_urls', views.SetUrlViewSet,basename='set_of_urls')
router.register(r'hits', views.HitViewset,basename='hits')

urlpatterns = [
    path('register/new_url',views.RegisterNewUrlView.as_view()),
    path('register/user',views.RegisterUserView.as_view()),
    path('user/', views.UserViewSet.as_view()),
    path('user/change_password/', views.ChangePasswordView.as_view(), name = 'change_password' ),  
    path('user/hits', views.UserHitsViewSet.as_view()),
    path('analytics/', include(api_analytics_urls)),
    path('', include(router.urls)),
]